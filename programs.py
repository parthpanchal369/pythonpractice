# 1. Hello world program in python                              1---------------------------------
# print("Hello World!")


# 2.  ADD two numbers program                              2-------------------------------------

# a = int(input("Enter your first number "))
# b = int(input("Enter your second number"))

# print("sum of two number is", a+b)
# print("minus of two number is ", a - b)
# print("Multiple of two number is: ",a * b)

# 3. Square root of the give number                         3---------------------------

# num1 = int(input("Enter your number: "))
# s1 = num1**(1/2)
# print("The square root of number is ", s1)

# import math
# num = int(input("Enter the number: "))
# s1 = math.sqrt(num)
# print(s1)

# 4. Python program to calculate area of triangle                  4------------------------------
# Height = float(input("Enter your height of triangle: "))
# base = float(input("Enter the base of triangle: "))
#
# area = (1/2)*Height*base
# print("Area of triangle is ", area)

#  5.Swap the value fo two variables                         5 ---------------------------
# x =12
# y = 14
# temp = x
# print("The value of temp = ", temp)
# x = y
# print("The value of x = ", x)
# y = temp
# print("the value of y = ",y)
#
# x = 12
# y = 14
#
# x,y = y,x
#
# print("The value of x = ",x , "The value of y = ",y)

# 6. Convert km to mile                                  6------------------------------
# km = float(input("Enter your km: "))
# miles = (0.621371)*km
# print(km, "kms to miles into ", miles)

# 7. number is positive or not                                   7----------------------------

# num = int(input("Ebter your number: "))
# if num > 0:
#     print("Your number is positive")
#
# elif num == 0:
#     print("your number is zero")
#
# else:
#     print("your number is negative")


# 8. number is odd or even                      8 ----------------------------

# num = int(input("Enter your number: "))
#
# if num % 2 ==0:
#     print("number is even")
#
# else:
#     print("number is odd")

# 9. Leap year or not                       9 ------------------------------

# num = int(input("Enter your year "))
#
# if (num % 400 == 0) and (num % 100 == 0):
#     print(num, "is a Leap year")
#
# elif (num % 4 ==0) and (num % 100 != 0):
#     print(num, "is a leap year")
#
# else:
#     print(num,"is not a leap year")


# def is_leap_year(year):
#
#     if (year % 400==0) and (year % 100 == 0):
#         return True
#     elif (year % 4==0) and ( year % 100 !=0):
#         return True
#
#     else:
#         return False
#
# is_year = int(input("Enter your year"))
#
# if is_leap_year(is_year):
#     print(f'{is_year} is a leap year')
#
# else:
#     print(f'{is_year} is a not leap year')

# 10.find the largest number among three number                       10--------------------------

# num1 = int(input("enter your first number: "))
# num2 = int(input("Enter your second number: "))
# num3 = int(input("Enter your third number: "))
#
# if num1 > num2 and num1 > num3:
#     print(num1,"YOur number is highest grater")
#
# elif num2 > num1 and num2 > num3:
#     print(num2,"your number is highest grater")
#
# else:
#     print(num3,"your number is highest grater")

# list1 = [1,2,3,4,5]
# max_number = max(list1)
# print(max_number)

# list1 = [5,3,6,9,5,7,2,4,45,3,2,4,45]
# sorted_number = sorted(set(list1))
# second_highest = sorted_number[-2]
# print(second_highest)
#
#
# list1 = [1,2,2,3,3,33,4,4,4,4,3]
# second_max_number = max([num for num in list1 if num != max(list1)])
# print(second_max_number)


# list1 = [2,4,3,6,7,4,5,9,90,45,34]
# sorted = sorted(set(list1))
# second_highest = sorted[-1]
# print(second_highest)


# 11. Prime number or not                             11---------------------
# num = int(input("Enter your number: "))
# if num <= 1:
#     print("It is a not a prime number")
#
# if num >1:
#     for i in range(2,num):
#         if num % i == 0:
#             print("It is not a prime number")
#             break
#
#     else:
#         print("It is a prime number")


# def prime_number(num):
#
#     if num < 2 :
#         return False
#
#     for i in range(2,num):
#         if num % i ==0:
#             return False
#
#     else:
#         return True
# num1 = int(input("Enter your number"))
#
# for numbers in range(1,num1):
#     if prime_number(numbers):
#         print(numbers)

# 12. generate random number program                     12------------------------------
# import random
# num = random.randint(0,6)
# print(num)


# 13. python program to print all prime numbers       13-------------------------

# lower = int(input("Enter your lower number: "))
# upper = int(input("Enter your upper number: "))
#
# for num in range(lower,upper+1):
#
#     if num > 1:
#
#         for i in range(2,num):
#             if num % i ==0:
#                 break
#
#         else:
#             print(num)

# 14. Python program to covert celsius to farenhit           14--------------
# c = int(input("Enter your celsius"))
# cf = c*(9/5) + 32
# print(cf)

# 15. Find the factorial of number               15----------------

# num = int(input("Enter your number: "))
#
# fact = 1
#
# if num < 0:
#     print("Factorial of less than 0 is dose not exist")
#
# if num == 0:
#     print("The factorial of 0 is ", 1 )
#
# if num > 0:
#     for i in range(1,num+1):
#         fact = fact*i
#
# print(f" The factorial of {num} is {fact}")

# Second method using recursion
# def fact(num):
#     if num == 0:
#         return 1
#
#     else:
#         return ((num) * fact(num-1))
#
# num1  = int(input("Enter your number: "))
# result = fact(num1)
# print(result)

# 16. Display the multiplication of table           16 --------------------

# num1 = int(input("Enter the number you want to table: "))
#
# for i in range(1,11):
#     print(f"{num1} x {i} = {num1*i}")

# num = int(input("Enter your number"))
# i = 0
# while i <= 10:
#     print(f"{num} x {i} = {num*i}")
#     i = i+1


# 17. Fibonacci sequence code            17-----------------------------

