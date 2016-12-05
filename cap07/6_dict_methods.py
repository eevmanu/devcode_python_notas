# /usr/bin/env python
# coding=utf-8

# ===============================================

dict_full = {
    'name': 'Alejandro Gomez',
    'age': 36,
    'address': 'Calle Los Camelios 215 - Urb. Alfajores'
}

# =================================================

print('dict_full[\'name\']: ', dict_full['name'])

dict_full['name'] = 'Enrique Palacios'
print('dict_full[\'name\']: ', dict_full['name'])

dict_full['DNI'] = '19876532'
print('dict_full[\'DNI\']: ', dict_full['DNI'])

del dict_full['DNI']
print('dict_full[\'DNI\']: ', dict_full['DNI'])

# =================================================

dict_len = len(dict_full)
print('len(dict_full): ', dict_len)

dict_value_ex_1 = dict_full.get('name')
print('dict_full.get(\'name\'): ', dict_value_ex_1)

dict_value_ex_1 = dict_full.get('DNI')
print('dict_full.get(\'DNI\'): ', dict_value_ex_1)

dict_value_ex_1 = dict_full.get('DNI', '----')
print('dict_full.get(\'DNI\'): ', dict_value_ex_1)

dict_has_key_ex_1 = 'DNI' in dict_full
print('\'DNI\' in dict_full: ', dict_has_key_ex_1)

# =================================================

dict_keys = dict_full.keys()
print('dict_full.keys(): ', dict_keys)
print('type(dict_keys): ', type(dict_keys))

list_keys = list(dict_keys)
print('type(list_keys): ', type(list_keys))

dict_values = dict_full.values()
print('dict_full.values(): ', dict_values)
print('type(dict_values): ', type(dict_values))

list_values = list(dict_values)
print('type(list_values): ', type(list_values))
