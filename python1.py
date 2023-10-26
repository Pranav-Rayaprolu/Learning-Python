# # super_hero_name=input("what is ur sph name tony bro?")
# # print("i am"+super_hero_name+"love you <3")
# # #sum of two numbers in python
# # x= int(input("number 1   "))
# # y= int(input("number 2   "))
# # sum = x+y
# # print(sum)
# # #strings
# # # method to convert all the characters of a string into uppercase letters
# name = "pranav"
# print(name.upper()) #it creates a new string and dont change the original one
# # method to convert all the characters of a string into lowercase letters
# print(name.lower())
# #method to find index of a substring in a string
# print(name.find("nav"))
# #gives starting index of the substring
# #returns -1 if there is no char mentioned
# #string manipulation
# print(name.replace("nav","veen")) #it doesnt change the original string
# ###keywords####
# #to check wether a character is in a string or not: use "in" keyword
# #it returns a boolean variable
# print("v" in name)
# ########          Arithmetic operators         ############
# print(5+2) #addition
# print(5-2) #subtraction
# print(5*2) #multiplication
# print(5/2) #division gives float i mean decimal values of quotient
# print(5**2) #exponential
# print(5//2) #gives only integer of quotient
# print(5%2) #gives remainder
# ########          Shortcuts         ############
# x=5
# x+= 2 # this means x=x+2
# print(x)
# x-= 2 # this means x=x-2
# print(x)
# x*= 2 # this means x=x*2
# print(x)
# x**= 2 # this means x=x**2
# print(x)
# ########         if statement         ############
# x=int(input("enter a number"))
# if(x>0):
#     print("the number is positive")
# elif(x<0):
#     print("the number is negative")
# else:
#     print("the number is zero")
# ########         logical operators         ############
# if(x>0 and x<3):
#     print("x is in range")
# if(x>0 or x<0):
#     print("it is ok buddy")
# ########         range function         ############
# x=range(5)#0,1,2,3,4
# # Print the numbers from 0 to 9
# print(range(10))

# # Print the even numbers from 0 to 10
# print(range(0, 11, 2))

# # Print the numbers from 10 to 0 in reverse order
# print(range(10, 0, -1))

# print(x)
# ########         while loop         ############
# i=1
# while(i<=5):
#     print(i)
#     i+=1
# ########         for loop         ############

# for i in range(5):
#     print(i)
# for i in range(5):
#     print(i+1)
# for i in range(5):
#     print(i*"*")
# for i in range(5,0,-1):
#     print(i*"*")
########         lists         ############
# It is a complex data type having a collection of primitive data types in it.
# synntax:
marks=[23,34,45,44,"maths",23.45]
print(marks)
#accessing the elements in the list
print(str(marks[4])[4])
#method to convert an integer into a string
#str()
#does typecasting happen in lists 
#yes when u include multiple data types in it
########         index         ############
# x="Pranav"
# print(x[1])
# print(x[-6]) #prints the last element that is v
# # 0   1  2  3  4  5 
# # P   r  a  n  a  v 
# # -6 -5 -4 -3 -2 -1
# ########         getting a sub list from a list using indexing         ############
# print(marks[0:2])#1st index including last index excluding
# # metho to add elements
# #1.at last is append()
# #2. at any position is insert()
# marks.append(55)
# print(marks)
# marks.insert(3,45)
# print(marks)
# # checking wether an element is in list or not
# print( 45 in marks) # it returns a boolean value true if there and vice versa
# #method to find the length of a list
# print(len(marks))
# print(marks)
# for mark in marks:
#     if mark >30:
#         print("fail")
#         break
#     print("meow")
    

# print(marks)
########         tuple         ############
# it is just like list but it is immutaable
# they dont even require braces
# frouits= "apple","banana","mango"
# print(frouits)
# marks= (99,98,99,99,95,96)
# #method to count a reperating leemnt
# print(marks.count(99))
# print(marks.index(98))
# ########         sets         ############
# # it is like list but has only unique elements
# dog={99,98,93,93,95}
# print(dog)
# # index do not exist in sets
# # list to set conversion
# x=set([1,2,2,2,3,4,5])
# print(x)
# ########         dictionary         ############
# # dictionary contains key value ppairs
# shoes ={"Nike":30,"adidas":45,"rebok":56}

# # it doesnt have the concept of indexing
# # elemnets can be accessed using key 
# # keys should always be unique
# print(shoes["Nike"])
# # to add a new pair in a dictionary
# shoes["Red Tape"] = 45
# print(shoes)
# # to change a values of an exsiting key
# shoes["Nike"]=34
# print(shoes)
########         functions         ############
# three typpes
# 1.inbuilt-int(),str(),bool()
# 2.Module-
    # set of similiar functions grouped together is called a module
    # import module_name
    # to get alll the functions in a specfic module use the following command
    # print(dir(module))
import math
print(dir(math))
    # to import a specific function from math
from math import sqrt
print(sqrt(4))
# 3.user defined
    #syntax
    # def function_name(parameters):
    # //do sth
# lets create a function to print sum of two numbers
def Twosum(a,b):
    print(a+b)
Twosum(1,2)

