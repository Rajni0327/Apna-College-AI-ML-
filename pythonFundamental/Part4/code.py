#  class ---------------------------------------------------
#  blueprint of an object


# object ----------------------------------------------------
# instance of a class
class student:
    subject = "python"
    college = "abc"
    year = "4th year"

    


stu1 = student()
stu2 = student()
print(stu1.subject, stu1.college, stu1.year)




# constructor  --------------------------------------------------
#  function that creates an object


# __init__method
# calls everytime when we create an object

# class Student:
#     def __init__(self):
#         print("constructor was called...")

# stu1 = Student()

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):   #stu1-as a reference , it will change for every object i.e stu1,stu2,stu3,stu4
        return self.cgpa

stu1 = Student("Sanaya", 8.0)
stu2 = Student("Sumitra", 7.8)
stu3 = Student("Ali", 6.9)
stu4 = Student("Mohit", 9.8)

print(stu1.name, stu1.cgpa)
print(stu2.name)
print(stu3.name)
print(stu4.name)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")


# types of constructors

# default = (self) 
# parameterized = (self, ... , ...)

# we can create only one constructor per class
# python does not supports multiple constructors like cpp and java , if we do so , it takes the last one by default





# Attributes -----------------------------------------------

# class attributes - belong to class --common 

# instance attribute - belong to object --unique,different

class Student:
    college_name = "ABC college" #class

    def __init__(self, name, cgpa):
        self.name = name #instance 
        self.cgpa = cgpa 


stu1 = Student("Sumita", 9.8)
print(stu1.name)
print(Student.college_name)  #this automatically calls the instance attributes


# instance attribute have higher priority than class attribute 
# if they have a same name attribute




# Product Store 
#design and create an online store for Products (name, price)
# track total products being created 
# create a static method to calculate discount on each product based on a % parameter


class Product:
    count= 0

    def __init__(self, name , price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):   #instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")

p1 = Product("phone", 10_000)
p2 = Product("laptop", 40_000)
p3 = Product("pen", 10)

p1.get_info()

Product.get_count()

p1.calc_discount(p1.price, 12)


