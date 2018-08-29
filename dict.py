# -*- coding: utf-8 -*-

data = {
    'title' : 'Sample Konfabulator Widget',
    'names' : ['name1', 'name2'],
    'width' : 500,
    'height' : 200.5465
}

#int float (str list dict set)

#dict:
# key - value
print(data.keys())

for i in data.keys():
    print(data[i])
    # data['names']