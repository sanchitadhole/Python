# String
# my_string = 'helloo'
# print(my_string)
# my_string = "hello"
# print(my_string)
# my_string = """hello"""
# # print(my_string)
#
# # ******************
# name = 'sanchita';
# length = len('name')
#
# i=0
# for n in range(-1,(-length-1),-1):
#     print(name[i],"\t",name[n])
#     i+=1
#
# # *************************
# msg1 = 'hellooo world'
# msg2 = 'python programming'
# print("msg1[0]:",msg1[0])
# print("msg2[1:5]:",msg2[1:5])
#
# # ********************************
# # Accessing value in string
# str = 'programming'
# print('str = ',str)
# print('str[0]=',str[0])
# print(str[1:5])
#
# #**************************
# # Updating String
# msg1 = 'hello world'
# print('updating string:',msg1[:6]+'python')
#
# # ***********************
# # string special operator
#
# # concatenation(+),
# # repetition(*),
# # slice[],
# # range of slice[:],
# # membership [in],
# # not in,
# # format %
#
# # eg.
# str1 = 'hello'
# str2 = 'sanchita'
# print('str1 + str2 :',str1,str2)
# print('str2*3 :',str2 * 3)
#
# # ***************************
# # string formating operator(%)
# print("my name is %s and weight is %d kg" %('sanchita',21))
#
# # ***************************
# # String Method

# capitalize()
name = 'sanchita is good girl'
print(name.capitalize())

# count()
x = name.count('is')
print(x)

# endswith()
y = name.endswith('c')
print(y)

# isalnum()
txt = 'company'
# a = txt.isalnum()
# print(a)

# isalpha()
# b =txt.isalpha()
# print(b)

# isdigit()
# c = txt.isdigit()
# print(c)

# islower()
d =txt.islower()
print(d)

# isnumeric()
e = txt.isnumeric()
print(e)

# isspace()
f = txt.isspace()
print(f)

# istitle()
txt2 = "Hello, And Welcome To My World"
g = txt2.istitle()
print(g)

# isupper()
h = txt.isupper()
print(h)

# join()
txt3 = ('sanchita','m','dhole')
i = '*'.join(txt3)
print(i)

# len()
j = len(txt)
print(j)

# ljust()
txt4 = 'banana'
h = txt4.ljust(12)
print(h, 'is my fav fruit')

# upper
k = txt.upper()
print(k)


# example
# String = input('enter a string')
# count = 0
# for i in String:
#     count = count+1
#
# new =String[0:2] + String[-2:]
# print('newly format string is:')
# print(new)

# *************************
# String = input('enter a string')
# print('Original String:',String)
# char = String[0]
# String = String.replace(char,'$')
# String = char + String[1:]
# print('replaced string:',String)

# ****************************

# string = input('enter a string')
# print('original string',string)
# string = string.replace('a','$')
# string = string.replace('A','$')
# print('replaced string:',string)

# *****************************
# str1 = input('enter first string')
# str2 = input('enter second string')
# new_a = str2[:2] + str1[2:]
# new_b = str1[:2] + str2[2:]
# print('the new swapping', (new_a +' '+ new_b))

# ********************************
# str2 = input('enter a string')
# print('string after swapping first and last character:',(str2[-1:]+str2[1:-1]+str2[:1]))

# ******************************
