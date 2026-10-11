import importlib
import os
import sys
import tempfile
import unittest

import k3ut

import k3modutil

dd = k3ut.dd


class TestModutil(unittest.TestCase):
    def setUp(self):
        sys.path.append(os.path.dirname(__file__))
        module_tree = [
            "root0",
            "root0.mod0",
            "root0.mod0.mod00",
            "root0.mod0.mod01",
            "root0.mod1",
            "root0.mod1.mod10",
            "root0.mod2",
            "root1",
            "root2",
            "root3",
            "root3.mod30",
        ]

        for module in module_tree:
            __import__(module)

    def tearDown(self):
        sys.path.remove(os.path.dirname(__file__))

    def test_submodules(self):
        test_cases = [
            (
                sys.modules["root0"],
                {
                    "mod0": sys.modules["root0.mod0"],
                    "mod1": sys.modules["root0.mod1"],
                    "mod2": sys.modules["root0.mod2"],
                },
            ),
            (sys.modules["root1"], {}),
            (sys.modules["root2"], None),
            # root3 is a namespace package: it has no __init__.py.
            (sys.modules["root3"], {"mod30": sys.modules["root3.mod30"]}),
            # An object without __path__ is not a package.
            ({}, None),
        ]

        for root, rst_expected in test_cases:
            dd("case: ", root, rst_expected)

            rst = k3modutil.submodules(root)
            dd("rst: ", rst)

            self.assertEqual(rst_expected, rst)

    def test_submodule_tree(self):
        test_cases = [
            (
                sys.modules["root0"],
                {
                    "mod0": {
                        "module": sys.modules["root0.mod0"],
                        "children": {
                            "mod00": {
                                "module": sys.modules["root0.mod0.mod00"],
                                "children": {},
                            },
                            "mod01": {
                                "module": sys.modules["root0.mod0.mod01"],
                                "children": None,
                            },
                        },
                    },
                    "mod1": {
                        "module": sys.modules["root0.mod1"],
                        "children": {
                            "mod10": {
                                "module": sys.modules["root0.mod1.mod10"],
                                "children": None,
                            },
                        },
                    },
                    "mod2": {
                        "module": sys.modules["root0.mod2"],
                        "children": None,
                    },
                },
            ),
            (
                sys.modules["root1"],
                {},
            ),
            (
                sys.modules["root2"],
                None,
            ),
            (
                {},
                None,
            ),
        ]

        for root, rst_expected in test_cases:
            dd("case: ", root, rst_expected)

            rst = k3modutil.submodule_tree(root)
            dd("rst: ", rst)

            self.assertEqual(rst_expected, rst)

    def test_submodule_leaf_tree(self):
        test_cases = [
            (
                sys.modules["root0"],
                {
                    "mod0": {
                        "mod00": {},
                        "mod01": sys.modules["root0.mod0.mod01"],
                    },
                    "mod1": {
                        "mod10": sys.modules["root0.mod1.mod10"],
                    },
                    "mod2": sys.modules["root0.mod2"],
                },
            ),
            (
                sys.modules["root1"],
                {},
            ),
            (
                sys.modules["root2"],
                None,
            ),
            (
                {},
                None,
            ),
        ]

        for root, rst_expected in test_cases:
            dd("case: ", root, rst_expected)

            rst = k3modutil.submodule_leaf_tree(root)
            dd("rst: ", rst)

            self.assertEqual(rst_expected, rst)

    def test_submodules_import_error(self):
        # The error that a submodule raises while it is imported reaches the caller unchanged.
        with tempfile.TemporaryDirectory() as tmp:
            os.mkdir(os.path.join(tmp, "broken"))
            with open(os.path.join(tmp, "broken", "__init__.py"), "w") as f:
                f.write("")
            with open(os.path.join(tmp, "broken", "bad.py"), "w") as f:
                f.write('raise RuntimeError("bad submodule")\n')

            sys.path.append(tmp)
            self.addCleanup(sys.path.remove, tmp)
            self.addCleanup(sys.modules.pop, "broken", None)
            importlib.invalidate_caches()

            broken = importlib.import_module("broken")
            with self.assertRaises(RuntimeError) as ctx:
                k3modutil.submodules(broken)

        self.assertEqual(("bad submodule",), ctx.exception.args)

    def test_submodule_tree_namespace_in_two_dirs(self):
        # A namespace package spread over two directories has the submodules of both.
        with tempfile.TemporaryDirectory() as dir_a, tempfile.TemporaryDirectory() as dir_b:
            for base, name in ((dir_a, "mod_a"), (dir_b, "mod_b")):
                os.mkdir(os.path.join(base, "spread"))
                with open(os.path.join(base, "spread", name + ".py"), "w") as f:
                    f.write("")

                sys.path.append(base)
                self.addCleanup(sys.path.remove, base)

            for mod in ("spread", "spread.mod_a", "spread.mod_b"):
                self.addCleanup(sys.modules.pop, mod, None)
            importlib.invalidate_caches()

            spread = importlib.import_module("spread")
            rst = k3modutil.submodule_tree(spread)

        expected = {
            "mod_a": {"module": sys.modules["spread.mod_a"], "children": None},
            "mod_b": {"module": sys.modules["spread.mod_b"], "children": None},
        }
        self.assertEqual(expected, rst)
