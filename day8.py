# Tuple

# tup1 = ('apple','banana',2020)
# tup2 = (1,2,3,4,5,6)
# tup3 = 'a','b','c','d'

# empty tuple
# my_tuple = ()
# print(my_tuple)

# tuple having integers
# my_tuple = (1, 2,3)
# print(my_tuple)

# nested tuple
# my_tuple = (1,2,3,['a','b','c'],(4,5,6))
# print(my_tuple)

# tuple can be created without parenthesis also called as tuple packing
# my_tuple = 3,3.2,'tybca'
# print(my_tuple)

# tuple unpacking
# a,b,c = my_tuple
# print(a)
# print(b)
# print(c)

# deleting tuple
# tup = ('apple', 'banana','mango')
# print(tup)
# del tup
# print('after deleting tuple:')
# print(tup)

# Deleting elements of Tuple
# tup1 = 'p','a','l','j','h','l',20
# print(tup1)
# tup1 = tup1[:2] +tup1[3:]
# print(tup1)
#
# lst = list(tup1)
# lst.remove('h')
# tup1 = tuple(lst)
# print(tup1)

# Basic Tuple Operations

# # 1. Addition(Concatenation)
# tup = (1,2,3) + (4,5,6)
# print(tup)
#
# # 2. Multiplication(Repetition)
# tup = 'Hiii!' * 4
# print(tup)
#
# # 3. Membership(in)
# tup = ('a','b''c')
# print('a' in tup)
#
# # 4.Iterating through a tuple
# for name in ('mom','dad'):
#     print('hello',name)



# Example

# l_range = int(input('enter the lower range'))
# u_range = int(input('enter the upper range'))
# a = [(x,x**2)for x in range(l_range,u_range+1)]
# print(a)

# *********************

tuplex =  1,5,6,8,2
print(tuplex)
tuplex = 5,
print(tuplex)

# *************************

tuplex = ('p','r','o','g','r','a','m','m','i','n','g')
str = ''.join(tuplex)
print(tuplex)
print(str)

# ******************************

tuplex = ('p','r','o','g','r','a','m','m','i','n','g')
print(tuplex)
a = tuplex[3]
print(a)
b = tuplex [-4]
print(b)

# *********************************
tuplex = ('q','d','d','k','u','k')
print(tuplex)
x = tuplex.count('d')
print(x)
# *********************************

tuplex = ('q','d','d','k','u','k')
print('r' in tuplex)
print('k' in tuplex)












