# Python Full-Spectrum Assessment
# Section 1: Python Basics & Control Flow
# Q1. Write a Python program to print all odd numbers between 10 and 50.

# for i in range (10,50):
#     if(i%2!=0):
#         print(i)


###########################################################################

# Q2. Create a function that returns whether a given year is a leap year.

# def leap(y):
#     if(y%4==0 and y%100!=0) or (y%400==0):
#         return f"{y} is a leap year"
#     else:
#         return f"{y} is not a leap year"
#
# print(leap(2025))
# print(leap(2024))

###############################################################################

# Q3. Write a loop that counts how many times the letter a appears in a given string.

# count=0
# str="app apple anaconda"
# for i in range(len(str)):
#     if str[i]=='a':
#         count+=1
# print(f"A appeared {count} times in string")

########################################################################3#####

# Section 2: Collections (Lists, Tuples, Sets, Dicts)
# Q4. Create a dictionary from the following lists:

# keys = ['a', 'b', 'c']
# values = [100, 200, 300]
# dictionary=dict(zip(keys,values))
# print(dictionary)

#################################################################################

# Q5. From a list of employee salaries, extract:
# The maximum salary
# All salaries above average
# A sorted version in descending order

# salary=[20000,30000,40000,50000]
# maximumsalary=max(salary)
# print(f"Higest salary: {maximumsalary}")
#
# averagesalary=sum(salary)/len(salary)
# print(f"Average salary: {averagesalary}")
#
# aboveaverage=[]
#
# for s in salary:
#     if(s>averagesalary):
#         aboveaverage.append(s)
#
# print(f"Above average salary{aboveaverage}")
#
# print("Sorted salary",sorted(salary,reverse=True))

#################################################################################

# Q6. Create a set from a list and remove duplicates. Show the difference between two
# sets:

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# setA=set(a)
# setB=set(b)
# print("setA: ",setA)
# print("setB: ",setB)
# print("set Difference A-B",setA-setB)

###############################################################################3

# Section 3: Functions & Classes
# Q7. Write a class Employee with __init__ , display() , and is_high_earner() methods.
# An employee is a high earner if salary > 60000.

# class Employee:
#     def __init__(self,name,dept,sal):
#         self.name=name
#         self.dept=dept
#         self.sal=sal
#     def display(self):
#         print(f"Name:{self.name}\nDepartment:{self.dept}\nSalary:{self.sal}")
#     def is_high_earner(self):
#         if(self.sal>60000):
#             return "High earner"
#         else:
#             return "Not an High earner"
#
# e=Employee("Aditya","DataEngineer",70000)
# print(e.display())
# print(e.is_high_earner())

#############################################################################

# Q8. Create a class Project that inherits from Employee and adds project_name and
# hours_allocated .

# class Employee:
#     def __init__(self,name,dept,sal):
#         self.name=name
#         self.dept=dept
#         self.sal=sal
# class Project(Employee):
#     def __init__(self,name,dept,sal,projectName,hoursAlloc):
#         super().__init__(name,dept,sal)
#         self.projectName=projectName
#         self.hoursAlloc=hoursAlloc
#     def displayProj(self):
#         print(f"project: {self.projectName},hoursAllocated: {self.hoursAlloc}")
# p=Project("aditya","aiml",60000,"bank fraud detection",7)
# p.displayProj()


###########################################################################################

# Q9. Instantiate 3 employees and print whether they are high earners.

# class Employee:
#     def __init__(self,name,dept,sal):
#         self.name=name
#         self.dept=dept
#         self.sal=sal
#     def display(self):
#         print(f"Name:{self.name}\nDepartment:{self.dept}\nSalary:{self.sal}")
#     def is_high_earner(self):
#         if(self.sal>60000):
#             return f"{self.name} is High earner"
#         else:
#             return f"{self.name} Not an High earner"
#
# e1=Employee("aditya","sde",50000)
# e2=Employee("barath","hr",70000)
# e3=Employee("Arun","ds",90000)
#
# emp=[e1,e2,e3]
# for e in emp:
#     print(e.is_high_earner())
#     print()

##########################################################################

# Section 4: File Handling
# Q10. Write to a file the names of employees who belong to the 'IT' department.

# employees=[
# {"name":"Aditya","dept":"IT"},
# {"name":"Varun","dept":"HR"},
# {"name":"Arun","dept":"IT"},
# {"name":"Tharun","dept":"SCM"},
# ]
#
# with open ("ITDept.txt","w") as file:
#     for e in employees:
#         if e["dept"]=='IT':
#             file.write(e["name"])

####################################################################

# Q11. Read from a text file and count the number of words.

# with open("ITDept.txt","r") as file:
#     t=file.read()
#     print(t)
#     words=t.split()
#     count=len(words)
#     print(f"Word Count:{count}")

##########################################################################

# Section 5: Exception Handling
# Q12. Write a program that accepts a number from the user and prints the square. Handle
# the case when input is not a number.


# try:
#     num=int(input("Enter the number:"))
#     print("Square of num is: ",num**2)
# except ValueError:
#     print("Only allowed to enter numbers")

################################################################################

# Q13. Handle a potential ZeroDivisionError in a division function.

# try:
#     a=int(input("Enter a :"))
#     b=int(input("Enter b :"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot divide by 0")

#######################################################################################

# Section 6: Pandas – Reading & Exploring CSVs
# Q14. Load both employees.csv and projects.csv using Pandas.

import pandas as pd
#
employees=pd.read_csv("employees.csv")
projects=pd.read_csv("projects.csv")

#Q15. Display:
# First 2 rows of employees
# Unique values in the Department column
# Average salary by department

# print(employees.head(2))
# print(employees["Department"].unique())
# print(employees.groupby("Department")["Salary"].mean())

###############################################################################3

# Q16. Add a column TenureInYears = current year - joining year.
# from datetime import datetime
# employees["JoiningDate"]=pd.to_datetime(employees["JoiningDate"])
# currentYear=datetime.now().year
# employees["TenureDate"]=currentYear-employees["JoiningDate"].dt.year
# print(employees[["Name","JoiningDate","TenureDate"]])

######################################################################################

#Section 7: Data Filtering, Aggregation, and Sorting
# Q17. From employees.csv , filter all IT department employees with salary > 60000.

# highSal=[]
# for index,e in employees.iterrows():
#     if (e["Department"]=="IT") and (e["Salary"]>60000):
#         highSal.append(e)
# print(highSal)

#############################################################################################

# Q18. Group by Department and get:
# Count of employees
# Total Salary
# Average Salary

# summary = employees.groupby("Department").agg(
#     EmployeeCount=('EmployeeID', 'count'),
#     TotalSalary=('Salary', 'sum'),
#     AverageSalary=('Salary', 'mean')
# )
#
# print(summary)



########################################################################################
# Q19. Sort all employees by salary in descending order.
#
# sortedempl=employees.sort_values(by="Salary",ascending=False)
# print(sortedempl)

###########################################################################################

# Section 8: Joins & Merging
# Q20. Merge employees.csv and projects.csv on EmployeeID to show project
# allocations.

# merged=pd.merge(employees,projects,on="EmployeeID",how="inner")
# print(merged)

##################################################################################################

# Q21. List all employees who are not working on any project (left join logic).

# emp_no_projects = pd.merge(employees, projects, on="EmployeeID", how="left")
# no_project_employees = emp_no_projects[emp_no_projects["ProjectID"].isnull()]
# print(no_project_employees)

################################################################################################3


# Q22. Add a derived column TotalCost = HoursAllocated * (Salary / 160) in the merged
# dataset.

# merged=pd.merge(employees,projects,on="EmployeeID",how="inner")
# merged["TotalCost"] = merged["HoursAllocated"] * (merged["Salary"] / 160)
# print(merged[["Name", "ProjectName", "HoursAllocated", "Salary", "TotalCost"]])
#

