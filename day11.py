# Function

# Defining a function

# def my_function(name):
#     print('hello from a functiom ' + name)
# def fun(str):
#     'i am sanchita'
#     print(str)
#     return


# Calling a function

# def my_function():
#     print('hello from a function')
# my_function()

# *******************

# Arguments
#
# def my_function(name):
#     print('hello '+ name)
# my_function('omkar')
# my_function('sanchita')
# my_function('snehal')

# *******************

# Number of arguments
# def my_function(fname, lname):
#     print(fname,'',lname)
# my_function('sanchita','dhole')
#
# # Arbitrary Arguments, *args
#
# def my_function(*kids):
#     print('the youngest child is' ,kids[2])
# my_function('sanchita','snehal','pranali')

# keyword arguments
# def my_function(child1, child2, child3):
#     print('the youngest child is '+ child3)
# my_function(child1='sanchita',child2='snehal',child3='pranali')\

# # Arbitrary keyword Argument, **kwargs
# def my_function(**kid):
#     print('his first name is ' + kid['fname'])
# my_function(fname = 'sanchita',lname = 'dhole')
#
# # Default parameter value
# def my_function(country = 'INDIA'):
#     print('I am from ' + country)
# my_function('Shrilaka')
# my_function('Amerika')
# my_function()
#
# # Passing a List as an Argument
# def my_function(food):
#     for i in food:
#         print(i)
# Fruits = ['mango','banana','chiku']
# my_function(Fruits)
#
# # Return value
# def my_function(x):
#     return 5 * x
#
# print(my_function(3))
