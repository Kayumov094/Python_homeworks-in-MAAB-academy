print("Welcome to lesson - 11")
######  file cretae qilish 
# import os
# operations = "operations"
# os.makedirs(operations, exist_ok=True)


#######  file ichiga __init__.py noml file create qildim 
# file_path = os.path.join(operations, "__init__.py")
# with open(file_path, "w") as file:
#     file.write("")

###### operations degan folder ichiga yana yangi file create qildim 
# file_path = os.path.join(operations, "file_readers.py")
# with open(file_path, "w") as file:
#     file.write("")

###### operations degan folder ichiga yana yangi file_writer.py degan file create qildim 
# file_path = os.path.join(operations, "file_writer.py")
# with open(file_path, "w") as file:
#     file.write("")

##### yangi file_ geometry degan folder yaratdim 

# file_geometry = "file_geometry"
# os.makedirs(file_geometry, exist_ok=True)

##### file_geometry ichiga yangi math_operations degan file ni cretae qilib oldim 
# file_path = os.path.join(file_geometry, "math_operations.py")
# with open(file_path, "w") as file:
#     file.write("")

###### file_geometry degan folder ichiga string_utils.py degan file ni create qildim
# file_path = os.path.join(file_geometry, "string_utils.py")
# with open(file_path, "w") as file:
#     file.write("")
 
###### file_geometry folderi ichiga python kodlarini yozamiz 

# folder = "file_geometry"  # dedimki mani folderim bu 
# file_path  = os.path.join(folder, "math_operations.py") # bu folderga yol bunday 
# # kodlari quyidagicha 
# code = """ 

# def add(a: int, b: int):
#     return a+b

# def substract(a: int, b: int):
#     return a - b

# def multiply(a: int, b: int):
#     return a*b

# def devise(a: int, b: int):
#     if b == 0:
#         return f"Nolga bo'lish mumkin emas"
#     else:
#         return a/b

# """
# with open(file_path, "w") as file: # open() funksiyasida foydalanib, yozish uchun och
#     file.write(code) # file ga quyidagi yoz dedim 

#### file_geometry folderi ichidagi ikkinchi string_utils.py degan filega kod yozamiz 
# folder = "file_geometry"
# file_path = os.path.join(folder, "string_utils.py")

# code = """
# def reverse_string(name: str):
#     return name[:: -1]

# def count_vowels(name : str ):
#     count = 0
#     for i in name.lower():
#         if i in ("a","o","u","e","i"):
#             count += 1
#     return count
# """
# with open(file_path, "w") as file:
#     file.write(code)

##### file_geometry folderi ichiga __init___.py file cretae qilamiz 
# folder = "file_geometry"
# file_path = os.path.join(folder, "__init__.py")

# with open(file_path, "w") as file:
#     file.write("")

###### file_geometry degan folder ichiga doira. py degan file create qilaman 

# folder = "file_geometry"
# file_path = os.path.join(folder, "doira.py")
# with open(file_path, "w") as file:
#     file.write("")
#### shu doira.py ichiga kod yozamiz 
# folder = "file_geometry"
# file_path = os.path.join(folder, "doira.py")

# code = """
# import math

# def calculate_area(radius:float):
#     return math.pi*radius**2

# def calculate_circumference(radius):
#     return 2*math.pi*radius
# """

# with open(file_path, "w") as file:
#     file.write(code)

##### endi operations degan folderdagi file_readers.py degan file ga kod yozamiz 
# folder = "operations"
# file_path = os.path.join(folder, "file_readers.py")
# code = """
# def read_file(file_path:str):
#     with open(file_path, "r") as file:
#         content = file.read()
#     return content
# """
# with open(file_path, "w") as file:
#     file.write(code)


#### endi operations degan folderning ichidagi file_writer.py degan filega kod yozamiz 
# folder = "operations"
# file_path = os.path.join(folder, "file_writer.py")
# code = """
# def read_file(file_path:str):
#     with open(file_path, "w") as file:
#         content = file.write()
#     return content
# """
# with open(file_path, "w") as file:
#     file.write(code)

 

# folder = r"F:\Arslonbek\MySecondBrain\DataAnalitika\Python_homework\lesson-11\homework\file_operations"
# print("Folder mavjudmi", os.path.exists(folder))
# print("Folder ichidagi files:", os.listdir(folder))
# print(os.getcwd()) # hozir qaysi papkada ekanligimni chiqaradi 

# print(geometry.doira.calculate_area(5))
