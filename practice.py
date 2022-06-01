# dict = {}
# n = int(input("enter dict elemment"))
# for i in range(n):
#     s = input("enter key")
#     v = input("enter value")
#     dict[s] = v
#
# test_case = int(input("enter test case"))
# for i in range(test_case):
#     for key in dict:
#         values = input()
#         if dict[key] == values:
#             print(key)

#Write a Python program to create an array using numpy of all the even integers from 1 to 100
import numpy as np
array = np.arange(1,104,2)
# print(array)

#Write a program to test whether none of the elements of a given numpy array is more than 100.
# for i in array:
#     if i>100:
#         print("flase")
#         break
#     else:
#         continue

# #Write a Python program to create an array with the integer values and determine the size of the memory occupied by the array. Comparison with list also.
#
# print("%d bytes" % (array.size * array.itemsize))
#
# #Write a NumPy program to create a NxN identity matrix. N is user entered positive Integer
# a = np.identity(4)
# print(a)
#
# #Write a Python program to remove all the numbers in a given array which is equal and greater to a given number
# target = 6
# for i in array:
#     if i> target:
#         array.re

# a = input()
# list = []
# for i in range(len(a)):
#     if (ord(a[i])>=65 and ord(a[i])<=90) or (ord(a[i])>=97 and ord(a[i])<=122):
#         list.append(a[i])
#
# def listToString(s):
#     # initialize an empty string
#     str1 = ""
#
#     # traverse in the string
#     for ele in s:
#         str1 += ele
#
#         # return string
#     return str1
# print(listToString(list))




# l=[('item1','12.20'),('item2','15.10'),('item3','24.5')]
# l2=[]
# l1=[]
# for i in l:
#     l1.append(i[1])
# l1.sort()
# for i in l1[::-1]:
#     for j in l:
#         if i in j:
#             l2.append(j)
# print(l2)


# l=[(),(),('',),('a','b'),('a','b','c'),('d')]
# l1=[]
# for i in l:
#     if len(i) != 0:
#         l1.append(i)
# print(l1)


# with open('harry.txt','wt') as f:
#     f.write("hi i am coding\n")
#     f.write("hi its me")
# with open('harry.txt') as f:
#     data = f.readlines()
#     data1 = f.readable()
#     print(data)
#     print(data1)
#
# import os
# os.remove("harry.txt")
# print("file del")


# with open('harry.txt','wt') as f:
#     f.write("hi i am coding\n")
#     f.write("hi its me")
# with open('harry.txt', 'rt') as f:
#     # data = f.read()
#     data1 = f.read(10)
#     # print(data)
#     # print(data[::-1])
#     print(data1)
#     print(data1[::-1])




# Write a Python program to read a random line from a file
# import random
# lines = open('harry.txt').read().splitlines()
# print(random.choice(lines))
f  = open('harry1.txt')
# with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
#
#     for line in firstfile:
#         secondfile.write(line)


