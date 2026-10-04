from importlib.metadata import version

__version__ = version("k3modutil")

from .modutil import (
    submodule_leaf_tree,
    submodule_tree,
    submodules,
)

__all__ = [
    "submodule_leaf_tree",
    "submodule_tree",
    "submodules",
]
