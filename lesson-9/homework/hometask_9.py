

print("Welcome to lesson 9 ")
print("Object Oriented Programming")

"""Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
Circleni ifodalovchi sinf yaratish uchun Python dasturini yozing. 
Uning maydoni va perimetrini hisoblash usullarini kiriting."""
import math # called math modul 
class Circle: # create Circle named class bu shablon hisoblanadi
 
    def __init__(self, radius): # doirsning xususiyatlarini yaratmoqchiman 
        self.radius = radius # doirada radius degan xusiyatini qo'shdim
        # shu bilan doiraga tegishli attrubitlar tugadi
    # endi Circle degan class ga method joriy qilmoqchiman      
    def circle_square(self):  # create method named circle_square 
        return f"Doiraning yuzi: {math.pi* self.radius **2}" #agar shu methodni ishlatsa manga shu javobni qaytar 
    
    def circle_perimetr(self): # create method named circle_perimetr 
        return f"Doiraning perimetri: {2*math.pi* self.radius}"#agar shu methodni ishlatsa manga shu javobni qaytar 
    
doira1 = Circle(5) # create object  
 

print(doira1.circle_perimetr())
print(doira1.circle_square())

"""2. Write a Python program to create a Person class. Include attributes like name, country, and date of birth. 
Implement a method to determine the person's age.
Person sinfini yaratish uchun Python dasturini yozing. Ism, mamlakat va tug'ilgan sana kabi atributlarni qo'shing. 
Shaxsning yoshini aniqlash usulini qo'llang."""
import datetime # import datetime module

class Person: #create Person class 
    def __init__(self, name, country, birthdate):  # create  some attributes
        self.name = name
        self.country = country
        self.birthdate = datetime.datetime.strptime(birthdate, "%d.%m.%Y").date()

    def person_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return f"This person's name is {self.name},\nThis person is from {self.country},\nThis person's birthdate is {self.birthdate}.\nFinally: Their age is {age}."

agent = Person("John", "USA", "20.11.1994")

print(agent.person_age())

import datetime 
class Person():
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = datetime.datetime.strptime(birthdate, "%d.%m.%Y").date()

    def person_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return f"This person's name is- {self.name},\nThis person is from {self.country},\nThis person's birthdate is {self.birthdate}.\nFinally: Their age is {age}."
agent1 = Person("John", "Tashkent", "18.08.1994")

print(agent1.person_age())
 
"""3. Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
Kalkulyator sinfini yaratish uchun Python dasturini yozing. Asosiy arifmetik amallar uchun usullarni kiriting."""
class Calculator: # create Calculator class 
    def __init__(self): 
        pass 

    def add(self, a, b): # made add() method 
        return a + b
    def subtract(self, a, b): # built substract()
        return a-b
    
    def mlt(self, a, b): # built mlt() method
        return a * b
    def devide(self, a, b): # built devvide() method 
        if b != 0:
            return a / b
        else:
            return f"Oh my God, ZerodevisionError"
    
calc = Calculator()
print(calc.add(10, 5)) # result 15
print(calc.subtract(10, 5)) # result 5
print(calc.mlt(10, 5)) # result 50
print(calc.devide(10, 5)) #result 2
print(calc.devide(10, 0)) # Oh my god, ZeroDevision Error
         
"""4. Write a Python program to create a class that represents a shape.
Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
Shaklni ifodalovchi sinf yaratish uchun Python dasturini yozing. Uning maydoni va perimetrini hisoblash usullarini kiriting.
Doira, uchburchak va kvadrat kabi turli xil shakllar uchun kichik sinflarni amalga oshiring."""
import math

class Shape:
    def area(self):
        pass
    def perimetr (self):
        pass 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Square of Circle {math.pi * self.radius ** 2}"
    
    def perimetr(self):
        return f"Perimetr of Circle {2 * math.pi * self.radius}"
    
class Square(Shape):
    def __init__(self, tomon):
        self.tomon = tomon

    def area(self):
        return f"Area of square {self.tomon * self.tomon}"
    
    def perimetr(self):
        return f"Perimetr of square {self.tomon*4}"
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        return f"Square of triangle {math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))}"
    def perimetr(self):
        return f"Perimetr of triangle {self.a + self.b + self.c}"
    
circle = Circle(5)
square = Square(10)
triangle = Triangle(3,4,5)

print(circle.area())
print(circle.perimetr())
print(square.area())
print(square.perimetr())
print(triangle.area())
print(triangle.perimetr())
 

""" 5. Write a Python program to create a class representing a binary search tree.
    Include methods for inserting and searching for elements in the binary tree.
    Ikkilik qidiruv daraxtini ifodalovchi sinf yaratish uchun Python dasturini yozing. 
    Ikkilik daraxtga elementlarni kiritish va qidirish usullarini qo'shing."""

class Node:
     def __init__(self, key):
          self.key = key
          self.left = None
          self.right = None

class BinarySearchTree:
     def __init__(self):
          self.root = None

     def insert(self, key):
          if self.root is None:
                self.root = Node(key)
          else:
                self._insert(self.root, key)

     def _insert(self, current_node, key):
          if key < current_node.key:
                if current_node.left is None:
                     current_node.left = Node(key)
                else:
                     self._insert(current_node.left, key)
          elif key > current_node.key:
                if current_node.right is None:
                     current_node.right = Node(key)
                else:
                     self._insert(current_node.right, key)

     def search(self, key):
          return self._search(self.root, key)

     def _search(self, current_node, key):
          if current_node is None:
                return False
          if current_node.key == key:
                return True
          elif key < current_node.key:
                return self._search(current_node.left, key)
          else:
                return self._search(current_node.right, key)

 
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print(bst.search(40))  # Output: True
print(bst.search(25))  # Output: False

"""6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
Stack ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing. Elementlarni surish va ochish usullarini qo'shing."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return f"Item {item} pushed to stack."

    def pop(self):
        if not self.is_empty():
            return f"Item {self.stack.pop()} popped from stack."
        else:
            return "Stack is empty. Cannot pop."

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return f"Top item is {self.stack[-1]}."
        else:
            return "Stack is empty."

# Example usage
my_stack = Stack()
print(my_stack.push(10))
print(my_stack.push(20))
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

"""7. Bog'langan ro'yxat ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing.
Bog'langan ro'yxat ma'lumotlarini ko'rsatish, tugunlarni kiritish va o'chirish usullarini qo'shing."""

class Tugun:
    def __init__(self, malumot):
        self.malumot = malumot
        self.keyingi = None

class BoglanganRoyxat:
    def __init__(self):
        self.bosh = None

    def kirit(self, malumot):
        yangi_tugun = Tugun(malumot)
        if not self.bosh:
            self.bosh = yangi_tugun
        else:
            joriy = self.bosh
            while joriy.keyingi:
                joriy = joriy.keyingi
            joriy.keyingi = yangi_tugun
        return f"{malumot} ma'lumotli tugun qo'shildi."

    def ochir(self, kalit):
        if not self.bosh:
            return "Ro'yxat bo'sh. O'chirish imkonsiz."
        if self.bosh.malumot == kalit:
            self.bosh = self.bosh.keyingi
            return f"{kalit} ma'lumotli tugun o'chirildi."
        joriy = self.bosh
        while joriy.keyingi and joriy.keyingi.malumot != kalit:
            joriy = joriy.keyingi
        if joriy.keyingi:
            joriy.keyingi = joriy.keyingi.keyingi
            return f"{kalit} ma'lumotli tugun o'chirildi."
        else:
            return f"{kalit} ma'lumotli tugun topilmadi."

    def korsat(self):
        if not self.bosh:
            return "Ro'yxat bo'sh."
        joriy = self.bosh
        natija = []
        while joriy:
            natija.append(joriy.malumot)
            joriy = joriy.keyingi
        return f"Bog'langan ro'yxat: {' -> '.join(map(str, natija))}"

# Misol uchun foydalanish
royxat = BoglanganRoyxat()
print(royxat.kirit(10))
print(royxat.kirit(20))
print(royxat.kirit(30))
print(royxat.korsat())
print(royxat.ochir(20))
print(royxat.korsat())
print(royxat.ochir(40))
print(royxat.korsat())

"""8. Xarid qilish savatini ifodalovchi sinf yaratish uchun Python dasturini yozing.
 Elementlarni qo'shish va olib tashlash va umumiy narxni hisoblash usullarini qo'shing."""

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item_name, price):
        self.cart.append({"item_name": item_name, "price": price})
        return f"Item '{item_name}' added to cart with price {price}."

    def remove_item(self, item_name):
        for item in self.cart:
            if item["item_name"] == item_name:
                self.cart.remove(item)
                return f"Item '{item_name}' removed from cart."
        return f"Item '{item_name}' not found in cart."

    def calculate_total(self):
        total = sum(item["price"] for item in self.cart)
        return f"Total price of items in cart: {total}"

    def show_cart(self):
        if not self.cart:
            return "Cart is empty."
        return "Items in cart:\n" + "\n".join([f"{item['item_name']}: {item['price']}" for item in self.cart])

 
cart = ShoppingCart()
print(cart.add_item("Apple", 1.5))
print(cart.add_item("Banana", 0.8))
print(cart.show_cart())
print(cart.calculate_total())
print(cart.remove_item("Apple"))
print(cart.show_cart())
print(cart.calculate_total())
 
"""9. Stack ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing. 
Elementlarni surish, ochish va ko'rsatish usullarini qo'shing."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return f"Item {item} pushed to stack."

    def pop(self):
        if not self.is_empty():
            return f"Item {self.stack.pop()} popped from stack."
        else:
            return "Stack is empty. Cannot pop."

    def show(self):
        if not self.is_empty():
            return f"Stack contents: {self.stack}"
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.stack) == 0

my_stack = Stack()
print(my_stack.push(10))
print(my_stack.push(20))
print(my_stack.show())
print(my_stack.pop())
print(my_stack.show())
print(my_stack.pop())
print(my_stack.pop())

"""10. Navbatdagi ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing. 
Elementlarni navbatga qo'yish va o'chirish usullarini kiriting."""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return f"Item {item} added to queue."

    def dequeue(self):
        if not self.is_empty():
            return f"Item {self.queue.pop(0)} removed from queue."
        else:
            return "Queue is empty. Cannot dequeue."

    def show(self):
        if not self.is_empty():
            return f"Queue contents: {self.queue}"
        else:
            return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

my_queue = Queue()
print(my_queue.enqueue(10))
print(my_queue.enqueue(20))
print(my_queue.show())
print(my_queue.dequeue())
print(my_queue.show())
print(my_queue.dequeue())
print(my_queue.dequeue())

"""11. Bankni ifodalovchi sinf yaratish uchun Python dasturini yozing.
Mijozlarning hisoblari va operatsiyalarini boshqarish usullarini qo'shing."""

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited. New balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount > 0:
            self.balance -= amount
            return f"{amount} withdrawn. New balance: {self.balance}"
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Account holder: {self.account_holder}, Balance: {self.balance}"

# Example usage
account = BankAccount("John Doe", 1000)
print(account.check_balance())
print(account.deposit(500))
print(account.withdraw(300))
print(account.withdraw(1500))
print(account.check_balance())