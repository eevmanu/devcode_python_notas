# /usr/bin/env python
# coding=utf-8

# ===============================================

dict_empty = {}
print(dict_empty)
print(type(dict_empty))
print(isinstance(dict_empty, dict))

# ===============================================

dict_full = {
    'name': 'Alejandro Gomez',
    'age': 36,
    'address': 'Calle Los Camelios 215 - Urb. Alfajores'
}
print(dict_full)
print(type(dict_full))
print(isinstance(dict_empty, dict))

# ===============================================

# import json
# print(json.dumps(dict_full, indent=4, sort_keys=True))
