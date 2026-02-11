# oop pillars 

# encapsulation
# abstraction
# inheritance
# polymorphism




# encapsulation
# wrapping data and functions into single unit

class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        #self._balance = balance  #protected accessed only in classes and sub classes
        self.__balance = balance  #private -data mangling

acc1 = BankAccount("Samarth Chauhan", 100_000)

print(acc1.name, acc1._balance)

# in python -when we create protected or private- it is by convention not enforced 