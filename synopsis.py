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
