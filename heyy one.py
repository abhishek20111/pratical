import math
import os
import random
import re
import sys





# dict = {"ghg":"ghh","fgy":68}
# for item,value in dict.items():
#     print(dict[item])
# """gffghghg bjkhj"""
# '''gujjh jjhhj'''
# print("bhjjhjhj jjj hi ---".__doc__)


# f = open("harry.txt","a")
# f.write("hi i am file\nhi hi hi")
# f.write("hoo")
#
# f.close()
# f = open("harry.txt","r")
# print(f.read())

# l =290
# def fun1(str):
#     l = 3
#     m = 9
#     print(str)
#     print(l)
#     print(m,"i am boy")
# fun1("jlfdjjkf jkfh")
# print(m)

# def sum(*args):
#     sum = 0
#     for item in args:
#         sum = sum+item
#     return sum
#
# if __name__ == '__main__':
#     a=sum(3,4,3,32,3,4,4,4,4,4,4,3,2322,3)
#     #print(type(a))
#     print(a)

# def filter_vowel(*letter):
#     vowel = ['a','e','i','o','u']
#     for i in letter:
#
#         if(i in vowel):
#             print("True")
#         else:
#             print("False")
#
# if __name__ == '__main__':
#     li = ["a","t","i"]
#     fil = filter_vowel(
#         li)
#     print(fil)


# def parnagram(str):
#     string = "abcdefghijklmnopqrstuvwxyz";
#     for element in string:
#        if element not in str.lower():
#            return False
#        return True
# if __name__ == '__main__':
#     str = input("Enter string")
#     value = parnagram(str)
#     if value is False:
#         print(" not paragram")
#     else:
#         print("paragram")
import os

if __name__ == '__main__':
    # list1 = list(map(int,input().split()))
    # for i in range(len(list1)):
    #     for j in range(len(list1)-1-i):
    #         if(list1[j]>list1[j+1]):
    #             tmp = list1[i]
    #             list1[i] = list1[i+1]
    #             list1[i+1] = tmp
    # print(list1[len(list1)-1])
    # a = int(input())
    # b = int(input())
    # c = list1[0]*(list1[0] > list1[1]) and list1[1]*(list1[0] < list1[1])
    # print(c)

    #------------------------
    # a = int(input())
    # b = int(input())

    # a>b and print(f'{a} is greater than {b}')
    # a<b and print(f'{b} is greater than {a}')
    # a==b and print(f'{b} is equal {a}')

    # a<b or print(f'{a} is greater than {b}')
    # a>b or print(f'{b} is greater than {a}')
    # a==b  and print(f'{b} is equal {a}')

    # print(f'{a} is greater'*(a>b))
    # print(f'{b} is greater'*(a<b))

    # a = int(input())
    # if a%4==0 and (a%400==0 or a%100!=0):
    #     print("leap year")
    # else:
    #     print("not leap year")



    # a = int(input())
    #
    # print(f"{a} is leap year"*(a % 4 == 0 and (a % 400 == 0 or a % 100 != 0)))
    # print(f"{a} is not leap year"*(a % 4 != 0 or (a%100==0 and a%400!=0)))

    # value = int(input())
    # li = [0]
    #
    # for i in range(value + 1):
    #     if i % 3 != 0:
    #         li.append(i)
    #         print(i)
    #     print("ghyggy",li[i])

    # m = input()
    # b = m.split()
    # c=''
    # for i in b:
    #     c+=i[::-1]
    #     c+=' '
    # print(c)

    # l1 = [3,24,32,3,2,3,43]
    # l2 = [43,32,2,2,3,54,5]
    # l=[]
    # l3=[]
    # for i in range(len(l1)):
    #     l.append(l1[i])
    #     l.append(l2[i])
    #     l3.append(tuple(l))
    #     l= []
    # print(l3)

    # n =4
    # for i in range(n,-1,-1):
    #     print(' '*(n-i)+'*'*(2*i+1))

    # strin = input()
    # li = []
    # for i in strin:
    #     li.append(i)
    #
    # l2 = []
    # for i in range(1,len(strin)):
    #     for j in range(1,len(strin)):
    #         if str[j+1] != str[j]:
    #             li.append(li[j])
    #             li.pop(j+1)

    # str = input()
    # str1 = str.upper()
    # si = str1[0]
    # print(si)
    # flag =0
    # for i in str1:
    #     if si != i:
    #         print("no")
    #         flag =1
    #         break
    # if flag ==0:
    #     print("hh")

    # value = list(map(int,input().split()))
    # l1 = []
    # for i in value:
    #     l1.append(value.count(i))
    # print(max(l1))

    # r = input()
    # l1=[chr(i) for i in range(65,91)]
    # fl=0
    # r2=r.upper()
    # for i in range(len(l1)):
    #     if l1[i] not in r2:
    #         print(" not pan")
    #         fl=1
    #         break
    # if(fl==0):
    #     print('pan')
    # n = 5
    # for i in range(1, n + 1):
    #     print(" "*(n-i)+"*"*(2*i-1))
    # for i in range(n,0,-1):
    #     print(" "*(n-i)+"*"*(2*i-1))

    def superReducedString(s):
        lis = []
        for i in s:
            lis.append(i)
        for i in range(len(lis)-1):
            if lis[i] == lis[i + 1]:
                lis.pop(i)
                lis.pop(i+1)
                #s.replace(s[i+1],"")
        if lis:
            print(lis,end="")
        else:
            print("Empty String")


    if __name__ == '__main__':
        #fptr = open(os.environ['OUTPUT_PATH'], 'w')

        s = input()

        result = superReducedString(s)


