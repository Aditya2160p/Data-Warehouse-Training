# VARIABLES, DATA TYPES, OPERATORS
# 1. Digit Sum Calculator Ask the user for a number and calculate the sum of its
# digits. Example: 753 → 7 + 5 + 3 = 15

# num = int(input("Enter a number: "))
# val=0
# while num>0:
#     digit=num%10
#     num=num//10
#     val=val+digit
#
# print("Sum of digits:", val)

# 2. Reverse a 3-digit Number Input a 3-digit number and print it reversed. Input:
# 123 → Output: 321
# num = int(input("Enter a number: "))
# rev=0
# digit=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
#
# print("reverse of digits:", rev)

# 3. Unit Converter Build a converter that takes meters and converts to:
# centimeters
# feet
# inches

# meters = float(input("Enter distance in meters: "))
# centimeters=meters*100
# feet=meters*3.281
# Inches=meters*39.37
# print(centimeters)
# print(feet)
# print(Inches)

# 4. Percentage Calculator Input marks of 5 subjects and calculate total, average,
# and percentage. Display grade based on the percentage.

# subjects = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
# total = sum(subjects)
# average = total / 5
# percentage = (total / 500) * 100
# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 75:
#     grade = "A"
# elif percentage >= 60:
#     grade = "B"
# elif percentage >= 45:
#     grade = "C"
# else:
#     grade = "Fail"
# print(f"Total: {total}, Average: {average}, Percentage: {percentage}%, Grade: {grade}")

# CONDITIONALS
# 5. Leap Year Checker A year is a leap year if it’s divisible by 4 and (not
# divisible by 100 or divisible by 400).

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# 6. Simple Calculator Input two numbers and an operator ( + - * / ) and perform the
# operation using if...elif...else .
#num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")
#
# if operator == '+':
#     print(f"Result: {num1 + num2}")
# elif operator == '-':
#     print(f"Result: {num1 - num2}")
# elif operator == '*':
#     print(f"Result: {num1 * num2}")
# elif operator == '/':
#     print(f"Result: {num1 / num2}")
# else:
#     print("Invalid operator")


# 7. Triangle Validator Given 3 side lengths, check whether they can form a valid
# triangle.

# a=int(input("Enter first side"))
# b=int(input("Enter second side"))
# c=int(input("Enter third side"))
# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")


# 8. Bill Splitter with Tip Ask total bill amount, number of people, and tip
# percentage. Show final amount per person.
# total = float(input("Enter total bill amount: "))
# people = int(input("Enter number of people: "))
# tip = float(input("Enter tip percentage: "))
#
# final_amount_per_person = (total + (total * tip/ 100)) / people
# print(f"Each person pays: {final_amount_per_person}")


# LOOPS
# 9. Find All Prime Numbers Between 1 and 100 Use a nested loop to check
# divisibility.

# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# 10.palindrome

# word = input("Enter a word: ")
# reverse = ""
#
# for char in word[::-1]:
#     reverse += char
#
# if word == reverse:
#     print("It's a palindrome!")
# else:
#     print("Not a palindrome.")


# 11.fibonacci series first n terms

# n = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# count = 0
#
# while count < n:
#     print(a, end=" ")
#     temp = a + b
#     a = b
#     b = temp
#     count += 1


# 12.Multiplication table

# num = int(input("Enter a number: "))
#
# for i in range(1, 10):
#     result = num * i
#     print(f"{num} x {i} = {result}")


# 13. Number Guessing Game
# Generate a random number between 1 to 100
# Ask the user to guess
# Give hints: "Too High", "Too Low"

# import random
#
# random = random.randint(1, 100)
# guess = 0
#
# while guess != random:
#     guess = int(input("Guess a number (1-100): "))
#     if guess > random:
#         print("Too high!")
#     elif guess < random:
#         print("Too low!")
#     else:
#         print("You guessed it!")



# 14.ATM Machine:


# balance = 10000
#
# while True:
#     print("\n1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")
#
#     choice = int(input("Select an option: "))
#
#     if choice == 1:
#         amount = float(input("Enter deposit amount: "))
#         balance += amount
#         print(f"New balance: {balance}")
#
#     elif choice == 2:
#         amount = float(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance -= amount
#             print(f"New balance: {balance}")
#         else:
#             print("Insufficient balance.")
#
#     elif choice == 3:
#         print(f"Current balance: {balance}")
#
#     elif choice == 4:
#         print("done")
#         break
#
#     else:
#         print("Invalid option.")


# 15.Password Strength Checker

# password = input("Enter a password: ")
#
# has_upper = False
# has_digit = False
# has_special = False
#
# for char in password:
#     if char.isupper():
#         has_upper = True
#     if char.isdigit():
#         has_digit = True
#     if char in "!@#$%^&*":
#         has_special = True
#
# if len(password) >= 8 and has_upper and has_digit and has_special:
#     print("Strong Password!")
# else:
#     print("Weak Password.")


# 16.GCD

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# while num2:
#     temp = num2
#     num2 = num1 % num2
#     num1 = temp
#
# print(f"GCD is: {num1}")
