# Add two number
# num1 = 2
# num2 = 6
# c = num1 + num2
# print(c)

# calculate square root
# num = float(input('enter a number:'))
# num_sqrt = num ** 0.5
# print('the square root of %0.3f is %0.3f'%(num,num_sqrt))
# print(num_sqrt)
# import math
# print(math.sqrt(-1))

# $$$$$$$$$$$$$$ Area of triangle $$$$$$$$$$$$$$$$$$$$
# a = float(input('enter first number'))
# b = float(input('enter second number'))
# c = float(input('enter third number'))
# s= (a+b+c)/2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('Area of a traingle is %f' %area)

# # $$$$$$$$$$$$$$$$$$$$ Swap two variables $$$$$$$$$$$$$$$
# a = input('enter value of a')
# b = input('enter value of b')
# temp = a
# a = b
# b = temp
# print('the value of a after swapping',a)
# print('the value of b after swapping',b)


# $$$$$$$$$$$$$$ random numer between 0 and 9$$$$$$$$$$$$$
#
# import random
# print(random.randint(0,9))



# $$$$$$$$$$$$$$$ dublicate or not $$$$$$$$$$$$$$
# n = input('enter five number')
# s1 = set(n)
# for i in s1:
#     c = n.count(i)
#     if c>1:
#         print('dublicate',i);
#     else:
#         print('unique',i)



# n= int(input('accept value'))
# if n in range(1,50):
#     print('ok')
# else:
#     print('out of range')

# $$$$$$$$$$$$$$$ sum of digit $$$$$$$$$$$$$$
# n = int(input('enter a number'))
# tot = 0
# while(n>0):
#     dig = n % 10
#     tot = tot + dig
#     n = n // 10
#
# print('the total sum of digit:', tot)

# $$$$$$$$$$$$$$$$$ fibonacci series $$$$$$$$$$$$$$

nterms = int(input('enter a number'))
n1= 0
n2=1
count = 0
if nterms<=0:
    print('enter positive interger')
else:
    print('fibonacci sequence upto',nterms)
    while count <  nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1



