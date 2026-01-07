# k3modutil

[![Action-CI](https://github.com/pykit3/k3modutil/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3modutil/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3modutil/badge/?version=stable)](https://k3modutil.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3modutil)](https://pypi.org/project/k3modutil)

Utilities for loading and inspecting Python submodules. Load all submodules of a package and build module trees.

k3modutil is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3modutil
```

## Quick Start

```python
import k3modutil
import mypackage

# Load all direct submodules of a package
submodules = k3modutil.submodules(mypackage)
# {'submod1': <module>, 'submod2': <module>, ...}

# Load all submodules recursively as a tree
tree = k3modutil.submodule_tree(mypackage)
# {'submod1': {'module': <module>, 'children': {...}}, ...}

# Load only leaf modules (no children)
leaves = k3modutil.submodule_leaf_tree(mypackage)
```

## API Reference

::: k3modutil

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
