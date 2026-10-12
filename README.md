# k3modutil

[![Action-CI](https://github.com/pykit3/k3modutil/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3modutil/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3modutil/badge/?version=stable)](https://k3modutil.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3modutil)](https://pypi.org/project/k3modutil)

Submodule Utilities.

k3modutil is a component of [pykit3] project: a python3 toolkit set.




# Install

```
pip install k3modutil
```

# Synopsis

```python
import xml

import k3modutil

k3modutil.submodules(xml)
# {
#     'dom': <module 'xml.dom' from '...'>,
#     'etree': <module 'xml.etree' from '...'>,
#     'parsers': <module 'xml.parsers' from '...'>,
#     'sax': <module 'xml.sax' from '...'>,
# }

k3modutil.submodule_tree(xml)
# {
#     ...
#     'parsers': {
#         'module': <module 'xml.parsers' from '...'>,
#         'children': {
#             'expat': {
#                 'module': <module 'xml.parsers.expat' from '...'>,
#                 'children': None,
#             },
#         },
#     },
#     ...
# }

k3modutil.submodule_leaf_tree(xml)
# {
#     ...
#     'parsers': {
#         'expat': <module 'xml.parsers.expat' from '...'>,
#     },
#     ...
# }
```

#   Author

Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>


[pykit3]: https://github.com/pykit3