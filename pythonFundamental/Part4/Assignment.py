# Answer 1----------------------------------------

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("amount withdrawn successfully")
        else:
            print("insufficient balance")

    def check_balance(self):
        print(f"your current bank balance is {self.balance}")

acc1 = BankAccount("11122", "Samay", 50_000)
acc1.deposit(10_000)
acc1.withdraw(20_000)
acc1.check_balance()


# Answer 2-----------------------------------------------
class Book:
    def __init__(self, title, author, list_of_reviews):
        self.__title = title 
        self.__author = author
        self.__list_of_reviews = list_of_reviews

    def add_new_review(self, new_review):
        self.__list_of_reviews.append(new_review)
        print("new review added successfully")

    def count_reviews(self):
        print(f"there are {len(self.__list_of_reviews)} reviews")

    def display_all_reviews(self):
        print("All the reviews are:")
        for review in self.__list_of_reviews:
            print("-", review)

    
b1 = Book("Rich Dad Poor Dad", "Rober T. Kiyosaki", ["a must read book"])

b1.add_new_review("Very helpful book")
b1.add_new_review("Simple and practical")

b1.count_reviews()
b1.display_all_reviews()



# Answer 3 ---------------------------------------------------

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = None
        self.__roll_no = None
        self.__marks = None

        # Use setter methods for validation
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks


    # Setter Methods 
    def set_name(self, name):
        if name.strip() == "":  #strip is a string function to remove the empty spaces
            print("Name cannot be empty.")
        else:
            self.__name = name

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative.")

s1 = Student("Samay", 99, 87)

print(f"name {s1.get_name()}")
print(f"marks {s1.get_marks()}")
print(f"roll no {s1.get_roll_no()}")

s1.set_marks(-10)   
s1.set_roll_no(150) 
s1.set_name("    ")     


# Answer 4-----------------------------------------------

class Shape:
    def area(self):
        print("Area method of Shape class")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # Overriding
        print(f"Area of Circle: {3.14 * self.radius * self.radius}")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):   # Overriding
        print(f"Area of Rectangle: {self.length * self.width}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):   # Overriding
        print(f"Area of Triangle:{ 0.5 * self.base * self.height}")


c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

c.area()
r.area()
t.area()


# Answer 5---------------------------------------

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

c1 = Car("mercedes","Benz", 5)
print(c1.brand, c1.model, c1.seats)

b1 = Bike("Apache","001", 155)
print(b1.brand, b1.model, b1.engine_cc)


# answer 6 --------------------------------------------------------

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


i1 = Intern(9000)
f1 = FullTimeEmployee(60000)
c1 = ContractEmployee(150, 500)

print(f"Intern Salary:{ i1.calculate_salary()}")
print(f"Full Time Salary:{ f1.calculate_salary()}")
print(f"Contract Salary:{ c1.calculate_salary()}")



# answer 7 -------------------------------------------------------

# Constructor overloading in Python is achieved using default arguments because Python does not support multiple constructors directly.

class Person :
    def __init__(self, name, age = None, address = None ):
        self.name = name
        self.age = age  
        self.address = address
    
    def display(self):
        print(f"Name:{ self.name}")
        print(f"Age:{ self.age}")
        print(f"Address:{ self.address}")
        print("-----------------------")

p1 = Person("Samay")
p2 = Person("Rudra", 26)
p3 = Person("Shlok", 23, "delhi")
p1.display()
p2.display()
p3.display()

         

# Answer 8 ---------------------------------------------

class Players:
    count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level

        Players.count += 1

    
p1 = Players("Samay", 9)
p2 = Players("Sushant", 7)
print(f"Total players are {Players.count}")


# Answer 9------------------------------------------------

class Herbivore:
    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

a1 = Bear("bear")
print(f"Animal : {a1.name}")
a1.eat_plants()
a1.eat_meat()
a1.eat_both()



# answer10 -------------------------------------

class User:   #user class
    def __init__(self, username):
        self.username = username

    def __str__(self):   # a method that controls how a object should looks when printed
        return self.username

class Message:   #message class
    def __init__(self, sender, content):
        self.sender = sender      # User object
        self.content = content

    def display(self):
        print(f"{self.sender}: {self.content}")

class ChatRoom:   #chatroom class
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []        # list of User objects
        self.messages = []     # list of Message objects
        print(f"{self.room_name }Chat room created")

    # User joins
    def join(self, user):
        self.users.append(user)
        print(f"{user} joined the chat.")

    # User leaves
    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user} left the chat.")
        else:
            print("User not in chat.")

    # Send message
    def send_message(self, user, content):
        if user in self.users:
            message = Message(user, content)
            self.messages.append(message)
        else:
            print("User must join the chat first.")

    # View chat history
    def view_history(self):
        print(f"\n--- Chat History of {self.room_name} ---")
        for message in self.messages:
            message.display()
        print("------------------------------------")

    
chat = ChatRoom("friends")

user1 = User("Samay")
user2 = User("Shrishti")

chat.join(user1)
chat.join(user2)

chat.send_message(user1 , f"hello shrishti! ")
chat.send_message(user2 , f"hiii samay! ")

chat.view_history()

chat.leave(user2)


# or 






# -------------------------------
# Message Class
# -------------------------------

class Message:
    message_counter = 1   # simple counter (class variable)

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


# ---------------------------------------
# Example Usage
# ---------------------------------------

if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
