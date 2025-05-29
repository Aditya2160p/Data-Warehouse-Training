# 1. Prime Number Checker
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n/2)+1):
#         if n % i == 0:
#             return False
#     return True
#
# print("Prime numbers between 1 and 100:")
# for i in range(1, 101):
#     if is_prime(i):
#         print(i, end=" ")
#
#############################################################33
# 2. Temperature Converter
# def convert_temp(value, unit):
#     if unit == "c":
#         return (value * 9/5) + 32
#     elif unit == "f":
#         return (value - 32) * 5/9
#     else:
#         return "Invalid unit"
#
# print(convert_temp(100, "c"))
# print(convert_temp(212, "f"))
################################################################3
# 3. Recursive Factorial Function
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(5))
##################################################################
#4.Class Rectangle
# class Rectangle:
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#     def area(self):
#         return self.l*self.w
#     def perimeter(self):
#         return 2*(self.l*self.w)
#     def is_square(self):
#         return self.l==self.w
#
# r=Rectangle(10,20)
# print(r.area())
# print(r.perimeter())
# print(r.is_square())

#####################################################################
# 6. Class: Book
# class BankAcc:
#     def __init__(self,name,bal):
#         self.name=name
#         self.bal=bal
#     def deposit(self,amount):
#         self.bal+=amount
#         print(f"{amount} is debited")
#     def withdraw(self,amount):
#         self.bal-=amount
#         print(f"{amount} is credited")
#     def get_bal(self):
#         print(self.bal)
# ba=BankAcc("aditya",1000)
# ba.deposit(500)
# ba.withdraw(200)
# ba.get_bal()
###################################################################33
#6.Class: Book
# class Book:
#     def __init__(self,title,author,price,in_stock):
#         self.title=title
#         self.author=author
#         self.price=price
#         self.in_stock=in_stock
#     def sell(self,quantity):
#         if quantity>self.in_stock:
#             print("we dont have that much books in stock")
#         else:
#             self.in_stock-=quantity
#             print(f"we have {self.in_stock} books in stock after your purchase of {quantity} books")
#
# b=Book("rich dad poor dad","robert kiyosaki",400,20)
# b.sell(5)
##############################################################################################3
#7.Student grade system
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
#     def grade(self):
#         avg = self.average()
#         if avg >= 90:
#             return "A"
#         elif avg >= 75:
#             return "B"
#         elif avg >= 50:
#             return "C"
#         else:
#             return "F"
# s=Student("aditya",(70,80,90,20,90))
# print(s.average())
# print(s.grade())
#############################################################################33
# 8. Person → Employee
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Employee(Person):
#     def __init__(self, name, age, emp_id, salary):
#         super().__init__(name, age)
#         self.emp_id = emp_id
#         self.salary = salary
#
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, ID: {self.emp_id}, Salary: {self.salary}")
# e1 = Employee("aditya", 21, "E0003", 50000)
# e1.display_info()
#######################################################################################

# 9. Vehicle → Car, Bike
# class Vehicle:
#     def __init__(self, name, wheels):
#         self.name = name
#         self.wheels = wheels
#
#     def description(self):
#         return f"{self.name} with {self.wheels} wheels"
#
# class Car(Vehicle):
#     def __init__(self, name, wheels, fuel_type):
#         super().__init__(name, wheels)
#         self.fuel_type = fuel_type
#
#     def description(self):
#         return f"{self.name} (Car) - {self.wheels} wheels, Fuel: {self.fuel_type}"
#
# class Bike(Vehicle):
#     def __init__(self, name, wheels, is_geared):
#         super().__init__(name, wheels)
#         self.is_geared = is_geared
#
#     def description(self):
#         geared = "Geared" if self.is_geared else "Non-geared"
#         return f"{self.name} (Bike) - {self.wheels} wheels, {geared}"
# v=Vehicle("hyundai",4)
# print(v.description())
# b=Bike("kawasaki",2,True)
# print(b.description())
# c=Car("skoda rapid",4,True)
# print(c.description())
##########################################################################################
# 10. Polymorphism with Animals

# class Animal:
#     def speak(self):
#         return "Some sound"
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# class Cow(Animal):
#     def speak(self):
#         return "Moo"
#
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     print(animal.speak())
####################################################################################