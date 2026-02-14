# oop pillars 

# encapsulation
# abstraction
# inheritance
# polymorphism




# # encapsulation -----------------------------------------------
# # wrapping data and functions into single unit

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name #public
#         #self._balance = balance  #protected accessed only in classes and sub classes
#         self.__balance = balance  #private -data mangling

#     def get_balance(self): #getter function
#         return self.__balance

#     def set_balance(self, newBalance): #setter
#         self.__balance = newBalance

# acc1 = BankAccount("Samarth Chauhan", 100_000)

# acc1.set_balance(200_000)

# print(acc1.name, acc1.get_balance())
# # or 
# print(acc1._BankAccount__balance) #access private value


# # in python -when we create protected or private- it is by convention not enforced 





# # Inheritance ----------------------------------------------
# # resuing attribute and methods from a parent(base) class

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"
    
#     def change_time(self, new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# t1 = Teacher("Math")
# t1.change_time("5pm")

# staff1 = AdminStaff("manager")

# print(t1.subject, t1.start_time, t1.end_time)
# print(staff1.role, staff1.start_time, staff1.end_time)


# # types
# # single level inheritance (aove is the example of single inheritance)

# # multi level inheritance
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#         def __init__(self, salary, role):
#             super().__init__(role)
#             self.salary = salary
    
# acc1 = Accountant(25_000, "CA")

# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

# # multiple inheritance

# # example a student who is a teacher also 

# class Teacher:
#      def __init__(self, salary):
#           self.salary = salary

# class Student:
#      def __init__(self, gpa):
#           self.gpa = gpa

# class TA(Teacher, Student):
#      def __init__(self, salary, gpa, name):
#           super().__init__(salary)
#           Student.__init__(self, gpa)
#           self.name = name

# ta1 = TA(15_000, 9.3, "Vishwas")

# print(ta1.name, ta1.gpa, ta1.salary)



# Abstraction ----------------------------------------
# means hiding internal details and showing only essential features