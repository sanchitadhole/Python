# Dictionary

# Empty Dictionary
# dict ={}
# print(dict)

# Dictionaty with integer key
# dict = {1:'apple',2:'orange'}
# print(dict)

# Dictionary with mixed keys
# dict = {'name':'abc',1:[1,2,3]}
# print(dict)

# using dict()
# dict = dict({1:'apple',2:'orange'})
# print(dict)

# from sequence having each item as a pair
# dict = dict([(1,'apple'),(2,'orange')])
# print(dict)

# Accessing Values in dictionary
# dict = {
#     'name':'sanchita',
#     'age' : 20
# }
# print("dict[name]:" ,dict['name'])
# print("dict[age]:" ,dict['age'])
#
# dict['name']= 'snehal'
# print(dict)

# Updating Dictionary
# dict.update({'color':'black'})
# print(dict)
# *******************

# for x in dict :
#     print(x)
#
# for x in dict :
#     print(x,dict[x])
#
# for x, y in dict.items():
#     print(x, y )

# Delete Dictionary element
# 1.del
# del dict['name']
# print(dict)

# dict.clear()
# print(dict)
#
# del dict
# print(dict)

# 2.clear()
# dict = {
#     'name':'sanchita',
#     'age' : 20,
#     'address':'pune',
#     'phone no':54522222
# }
# dict.clear()
# print(dict)

# # 3.pop()
# dict = {
#     'name':'sanchita',
#     'age' : 20,
#     'address':'pune',
#     'phone no':54522222
# }
# dict.pop('address')
# print(dict)
#
# # 4.popitem()
# dict = {
#     'name':'sanchita',
#     'age' : 20,
#     'address':'pune',
#     'phone no':54522222
# }
# dict.popitem()
# print(dict)

# ***************************
# d = {0:'a',1:'a',2:'a',3:'a'}
# print(d)
# print(d[0]==d[1]==d[2])

car = {
    'brand' : 'ford',
    'model' : 'Mustang',
    'year': 1979
}

for n in car:
    print(n,car[n])

x = car.keys()
y = car.values()
car['color'] = 'white'
print(x)
print(y)
print(x,y)

# example
d = {0:10,1:20}
print(d)
d.update({3:30})
print(d)




