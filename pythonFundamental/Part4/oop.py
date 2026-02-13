# oop pillars 

# encapsulation
# abstraction
# inheritance
# polymorphism




# # encapsulation
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





# Inheritance
# resuing attribute and methods from a parent(base) class

