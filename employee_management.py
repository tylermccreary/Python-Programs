#employee_management.py
#A program to manage employees.
#Author: Tyler McCreary

import math

#A class representing an employee
class Employee:
    def __init__ (self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    def pay_raise (self, department, percent):
        if self.department == department:
            self.salary = int((1 + int(percent)/100) * self.salary)
    def pay_cut (self, department, percent):
        if self.department == department:
            self.salary = int((1 - int(percent)/100) * self.salary)
    def __str__ (self):
        return str(self.name) + ", " + str(self.department) + ", " + str(self.salary)


def main():
    employees = []
    user_input = "not finished"
    while(user_input != "finish"):
        user_input = input("Add, raise, cut, or finish? ")
        if user_input == "add":
            name = input("Name? ")
            dep = False
            while not dep:
                department = input("Department? ")
                department = department.split()
                if len(department) == 1:
                    department = department[0]
                    dep = True
                else:
                    print("Error. Department must be one word")
            sal = False
            while not sal:
                salary = input("Salary? ")
                if int(salary) >= 0:
                    salary = int(salary)
                    sal = True
                else:
                    print("Error. Salary must be a positive integer.")
            employees.append(Employee(name, department, salary))

        elif user_input == "raise":
            department = input("Department? ")
            percent = False
            while not percent:
                percentage = input("Percentage? ")
                if (int(percentage) <= 100 and int(percentage) >= 0):
                    percent = True
                else:
                    print("Error. Please enter an integer between 0 and 100.")
            for i in range(len(employees)):
                employees[i].pay_raise(department, percentage)
        elif user_input == "cut":
            department = input("Department? ")
            percent = False
            while not percent:
                percentage = input("Percentage? ")
                if (int(percentage) <= 100 and int(percentage) >= 0):
                    percent = True
                else:
                    print("Error. Please enter an integer between 0 and 100.")
            for i in range(len(employees)):
                employees[i].pay_cut(department, percentage)
        elif user_input == "finish":
            for i in range(len(employees)):
                print(employees[i])
        else:
            print("Error: Please enter add, raise, cut or finish")
    
main()
