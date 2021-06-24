# List - mutable

# list1 = ['sanchita',21,55.1,]
# print(list1)
#
# list12 = ["apple","banana","cherry"]
# print(list12)

list1 = [1,2,3,4,5]
print(list1[0])
print(list1[0:2])
print(list1[:-1])

# updating list
list1[2] = 8
print(list1)

# Append element
list1.append(9)
print(list1)

# deleting list
list3 = ['java','python','javascript']
print(list3)
# del (list3[1])
# print(list3)

list3.remove('python')
print(list3)

# Basics List Operations
# 1.length
a = len([4,8,5,3,5])
print(a)
# 2.concatenation
b = [1,2,3,]+[5,8,6]
print(b)
# 3.Repetition
c= ['hi']*3
print(c)
# 4.Membership
d = 3 in [1,5,3]
print(d)
# 5.Iteration
for i in [1,3,5]:
    print(i)

# Reverse a List
# myList = [1,2,8,9,45]
# myList.reverse()
# print(myList)

# for item in reversed(myList):
#     print(item)

# print(myList[::-1])


from array import *
T =[[11,12,5,2],[15,6,10],[41,54,58,5],[2,5,5,5]]
for r in T:
    for c in r:
        print(c,end=" ")
    print(c)



