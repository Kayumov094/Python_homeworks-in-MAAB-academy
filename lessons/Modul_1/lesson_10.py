# print("Hello, World!")
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# xabar = "hammasi yaxshi"
# surish = 3
# for i in xabar:
#     if i in alphabet:
#         index = alphabet.index(i)
#         new_index = (index + surish) % len(alphabet)
#         print(alphabet[new_index], end = "")
#     else:
#         print(i, end = "")
# import os
# file_path = "test.txt"
# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content.split())

# print(len(content))
# #     print(i)

class Restaurant():
    def __init__(self, restaurant_name, type_cook):
        self.restaurant_name = restaurant_name
        self.type_cook = type_cook

    def describe(self):
        print(f"Restaurant nomi {self.restaurant_name} bo'lib, unda {self.type_cook} taomlar tayyorlanadi")

restaurant1 = Restaurant("Rayhon", "milliy")
restaurant2 = Restaurant("Yapona Mama" , "yaponcha")

restaurant1.describe()
restaurant2.describe()




     