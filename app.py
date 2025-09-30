# # loops
# # for Loop
# # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # for x in fruits:
# #     print(x)

# # # While Loop
# # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # while "kiywi" in fruits:
# #     print("kiwi is in the list")

# # name = "Obinna"
# # for j in name:
# #     print(j)


# # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # for x in fruits:
# #     if "banana" == x:
# #         print("yes, banana is present")
# #     else:
# #         print("loop continues")

# # if "banana" in fruits:
# #     print("yes, banana is present")
# # else:
# #     print("no, banana is not present")

# # age = 5
# # while age < 10:
# #     print("you are a tudler")
# #     age += 1
# # print("you are now an minor")
# # first_array = [1, 2, 3, 4, 5]
# # second_array = [6, 5, 4, 3, 6, 7, 5, 4, 9, 89]
# # sorted_array = sorted(first_array + second_array)
# # print(sorted_array)

# # a = {1, 2, 3, 4, 5}
# # b = {4, 2, 2, 1, 5, 1, 6}
# # # print(a)
# # print("a union b:", a.union(b))
# # print("a union b:", a | b)
# # print("a intersection b:", a.intersection(b))
# # print("a intersection b:", a & b)
# # print("a Difference b", a - b)
# # print("a Difference b", a.difference(b))
# # print("b Difference a", b - a)
# # print("b Difference a", b.difference(a))


# # person = {
# #     "Name": "Obinna",
# #     "Age": 23,
# #     "Country": "Nigeria",
# #     "Hobbies": ["Reading", "Coding", "Football"],
# #     "gender": "Male",
# #     "Intrests": ["Technology", "Art", "Music"],
# # }
# # print(person)["Name"]
# # print(person)["Hobbies"]

# # for key, value in person.items():
# #     print(f"{key}: {value}")

# # def greeting(firstName="John", lastName="Mark", age=50):
# #     print(
# #         f"Hello, my name is, {firstName}, {lastName}. im,{age}years old, Welcome to Python  🐍!")
# # print(f"Welcome Back, {firstName} {lastName} to Python 🐍!")


# # greeting("Obinna", "Agu", 23)
# # def SumTwoNumbers(num1=10, num2=10):
# #     return num1 + num2


# # result = SumTwoNumbers(20, 30)
# # print(result)

# name = "JohnBoscoe"


# def userGrade(grade1, grade2, grade3):
#     print("Science", grade1, "English", grade2, "Maths", grade3, )
#     JohnBoscoe = (grade1 + grade2 + grade3) / 3
#     if JohnBoscoe >= 70:
#         return "A, You sabi book"
#     elif JohnBoscoe >= 60:
#         return "B, You dey try"
#     elif JohnBoscoe >= 50:
#         return "C, Omoo you need to work harder"
#     elif JohnBoscoe >= 40:
#         return "D, E remain small you for fail"
#     else:
#         return "F, You don fail, better luck next time"


# result = userGrade(50, 60, 90)
# print(f"{name}, your average result is {result} ")

# result2 = userGrade(20, 30, 40)
# print(f"James, your average result is {result2} ")
# result3 = userGrade(70, 80, 90)
# print(f"Mary, your average result is {result3} ")
# result4 = userGrade(10, 20, 30)
# print(f"Paul, your average result is {result4} ")
# result5 = userGrade(40, 50, 60)
# print(f"Susan, your average result is {result5} ")
# result6 = userGrade(90, 80, 70)
# print(f"Peter, your average result is {result6} ")


# ____________LIST COMPRENSHION_____________________
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)
# cubed_numbers = [num ** 3 for num in numbers]
# print(cubed_numbers)
# double_numbers = [num * 2 for num in numbers]
# print(double_numbers)

# salaries = [200000, 100000, 700000, 800000, 900000]
# increment = []
# for salary in salaries:
#     NewSalary = salary + (salary*0.25)
#     increment.append(NewSalary)
# print(increment)
# ____________LIST COMPRENSHION_____________________
# values = [10, 20, 30]
# newValues = [value*2 for value in values]
# print(newValues)

# values = [10, 20, 30]
# newValues = []
# for value in values:
#     newValue = value*2
#     newValues.append(newValue)
# print(newValues)
# _______________Built in Modules____________________
from datetime import datetime
import random
import math
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
print(math.ceil(4.2))
print(math.cos(90))

# ___________RANDOM MODULE____________________
print(random.randint(1, 100))
print(random.choice(["apple", "banana", "cherry"]))
print(random.random())

print(datetime.now())
