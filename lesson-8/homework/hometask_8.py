print("Hello Arslonbek! Welcome to 8 lesson")
""""1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
ZeroDivisionError Raqamni nolga bo'lishda istisnolarni hal qilish uchun Python dasturini yozing ."""
# def devisor(): # create devisor named function 
#     a = 10 # create variable
#     b = 0 # create variable
#     try:
#         print(f"result is {a/b}") # t
# ry print this message 
#     except ZeroDivisionError: if devisor equal zero
#          print("Devisor must not  be zero ") # print this massage
# devisor() # I use the function
 

"""2. Write a Python program that prompts the user to input an integer and raises a ValueError
 exception if the input is not a valid integer.
 Foydalanuvchini butun sonni kiritishni taklif qiladigan va ValueErroragar 
 kiritilgan butun son bo'lmasa, istisno keltiradigan Python dasturini yozing."""
 
# try:
#     number = int(input("Please input integer number: ")) # try to do this steps
#     print(f"You entered number {number}") # then print message 
# except ValueError: # if valueerrror
#     print("You entered Value is not integer") # print this message 

 


"""3. Write a Python program that opens a file and handles a FileNotFoundError exception 
if the file does not exist
Faylni ochadigan va FileNotFoundError agar fayl mavjud bo'lmasa, istisnolarni boshqaradigan Python dasturini yozing."""

# try:
#     file_name = input("Please enter your file: ") # enter file_name by user 
#     with open(file_name, 'r') as file: # open() built in function in Python
#         content = file.read() # used function read() for file and equaled content variable 
#         print("File content") # said print thos message 
#         print(content) # said print content variable 
# except FileNotFoundError: # if File not found
#     print("Execuse me, file not found! Try again" ) # said print this message 

"""Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
Python dasturini yozing, u foydalanuvchidan ikkita raqamni kiritishni taklif qiladi va TypeError agar kirishlar sonli bo'lmasa, istisno qiladi."""
 
# def get_number(prompt):
#     value = input(prompt)     # Raqam yoki o'nlik son bolmasa
#     if not value.replace('.', '', 1).isdigit():
#         raise TypeError("Input must be a number!")
#     return float(value)  # float yoki int ga aylantirish

# try:
#     number_first = get_number("Please enter first number: ")
#     number_second = get_number("Please enter second number: ")
#     print(f"Your numbers sum is: {number_first + number_second}")
# except TypeError as e:
#     print(f"Error: {e}") # print this message 

""" 5 .Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
PermissionErrorAgar ruxsat bilan bog'liq muammo bo'lsa, faylni ochadigan va istisnolarni boshqaradigan Python dasturini yozing ."""
# try:
#     file_name = input("Please your file name: ")
#     with open(file_name, 'a') as file:
#         file.write("Hello")
#     print("write successfully")
# except PermissionError:
#     print("Your don't have Permission write this file")
# except FileNotFoundError:
#     print("Error: File not found. Please check the file name.")

"""6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
Ro'yxatda amalni bajaradigan va IndexErrorindeks diapazondan tashqarida bo'lsa, istisnolarni bajaradigan Python dasturini yozing."""

# try:
#     first_list = [1 , 2 , 3 , 4] #create first_list
#     error = first_list[6] # call value that without range list and equaled error variable 
#     print(f"Result list is {error}") #print this message 
# except IndexError as e: #else 
#     print(f"{e}") # print error name 

"""7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
Foydalanuvchiga raqam kiritishni taklif qiladigan va KeyboardInterrupt agar foydalanuvchi kiritishni bekor qilsa, 
istisnoni hal qiladigan Python dasturini yozing."""
# try:
#     while True:
#         x = input("Please enter your Card pin code: ")
#         print(f"Your pin code {x}")
# except KeyboardInterrupt: # when user stoped manually 
#     print("\n Program interupted by user")

"""8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
ArithmeticError Agar arifmetik xato bo'lsa, bo'linishni bajaradigan va istisnolarni bajaradigan Python dasturini yozing ."""
# try:
#     a = 5
#     b = 0
#     result = a / b 
#     print(f"The answer to the question {result}") # print this message 
# except ArithmeticError: # if Arithmetic error
#     print(" Oh my God, your have Arithmetic error") # print this message

"""9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
UnicodeDecodeError Agar kodlash muammosi bo'lsa, faylni ochadigan va istisnolarni hal qiladigan Python dasturini yozing ."""
# try: 
#     file_name = input("Please enter your file name: ")
#     with open(file_name, 'r', encoding = 'utf-9') as file:
#         content = file.read()
#         print("File successfully open!")
#         print(content)
# except UnicodeTranslateError:
#     print("Oh my God, Your have unicode Error")
# except FileNotFoundError:
#     print("File not found")


""""10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
Ro'yxat amalini bajaradigan va AttributeError agar atribut mavjud bo'lmasa, istisnolarni boshqaradigan Python dasturini yozing."""
# try:
#     a = 5
#     result = a.append(10)
#     print(f"result of program {result}")
# except AttributeError:
#     print("Oh my God, you have AttributeError")

"""Python File Input Output: Exercises, Practice, Solution"""
"""1. Write a Python program to read an entire text file.
Butun matn faylini o'qish uchun Python dasturini yozing."""
 
# def read_text(file_name):
#     try:
#         with open (file_name, 'r') as file:
#             content = file.read()
#         return content
#     except FileNotFoundError:
#         return "Error: Oh my God!" 


# file_name = "my_text_file.txt"
# print(read_text(file_name))


"""2. Write a Python program to read first n lines of a file.
n Faylning birinchi qatorlarini o'qish uchun Python dasturini yozing ."""

# def read_file_line(file_name, n):
#     try:
#         with open(file_name, 'r', encoding = "utf-8") as file:
#             lines = []
#             for i in range(n):
#                 line = file.readline()
#                 if not line:
#                     break
#         return lines
#     except FileNotFoundError:
#         return "Error: File not found!"

# file_name = "my_text_file.txt"
# n = 3   
# print(read_file_line(file_name, n))

# file_name = "my_text_file.txt"
# print(read_file_line(file_name))

"""3. Write a Python program to append text to a file and display the text.
Faylga matn qo'shish va matnni ko'rsatish uchun Python dasturini yozing."""
# file_name = "my_text_file.txt"

# try:
#     text_to_append = input("Enter text to append to the file: ")
#     with open(file_name, 'a', encoding="utf-8") as file:
#         file.write(text_to_append + "\n")  # yangi qator sifatida qo'shadi
#     with open(file_name, 'r', encoding="utf-8") as file:
#         content = file.read()

#     print("\nUpdated file content:")
#     print(content)
# except FileNotFoundError:
#     print("Error: File not found!")
 
"""4. Write a Python program to read last n lines of a file.
 nFaylning oxirgi satrlarini o'qish uchun Python dasturini yozing ."""
# def read_last_n_lines(file_name, n):
#     try:
#         with open(file_name, 'r', encoding="utf-8") as file:
#             lines = file.readlines()  # fayldagi barcha qatorlarni ro'yxatga oladi
#         return [line.strip() for line in lines[-n:]]  # oxirgi n qatorni olish
#     except FileNotFoundError:
#         return "Error: File not found!"
#     except UnicodeDecodeError:
#         return "Error: Cannot decode file due to encoding issues."

# file_name = "my_text_file.txt"
# n = 3  # oxirgi 3 qatorni o'qish
# print(read_last_n_lines(file_name, n))

"""Write a Python program to read a file line by line and store it into a list.
Faylni satr bo'yicha o'qish va uni ro'yxatga saqlash uchun Python dasturini yozing."""

# def read_file_by_line(file_name):
#     try:
#         list_file = []
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 list_file.append(line)
#         return list_file
#     except FileNotFoundError:
#         print("File not found")
# file_name = "my_name_is_Arslonbek.txt"

# print(read_file_by_line(file_name))

# # 2- example 
# def read_file_by_line(file_name):
#     try:
#         with open(file_name, 'r', encoding="utf-8") as file:
#             return [line.strip() for line in file] # list comprehension 
#     except FileNotFoundError:
#         return "Error: File not found!"
#     except UnicodeDecodeError:
#         return "Error: Cannot decode file due to encoding issues."

# file_name = "my_name_is_Arslonbek.txt"
# print(read_file_by_line(file_name))

"""6. Write a Python program to read a file line by line and store it into a variable.
Faylni satr bo'yicha o'qish va uni o'zgaruvchiga saqlash uchun Python dasturini yozing."""

# def read_file_store_in_variable(file_name):
#     try:
#         store = []  # create list
#         with open(file_name, 'r') as file:
#             for line in file:  # faylni satrma-satr o'qish
#                 store.append(line.strip())  # \n ni olib tashlash
#         return store  # ro'yxatni qaytarish
#     except FileNotFoundError:
#         return "Oh my God, error! File not found."

# file_name = "my_file.txt"
# print(read_file_store_in_variable(file_name))


"""Write a Python program to read a file line by line and store it into an array.
Faylni satr bo'yicha o'qish va uni massivda saqlash uchun Python dasturini yozing."""

# import numpy as np # call numpy library
# def read_file_store_in_array(file_name): #cretae function 
#     try: 
#         my_list =  [] # cretae empty list 
#         with open(file_name, 'r') as file: # open file with r mode
#             for line in file:
#                 my_list.append(line.strip())  # \n ni olib tashlaymiz
#         my_array = np.array(my_list)  # ro'yxatdan NumPy array yaratish
#         return my_array
#     except FileNotFoundError:
#         return "Oh my God, error! File not found!!!!!."

# file_name = "my_file.txt"
# print(read_file_store_in_array(file_name))  
 

"""8. Write a Python program to find the longest words.
Eng uzun so'zlarni topish uchun Python dasturini yozing.""" 

# word_one = input("Please enter a word any length: ")
# word_second = input("Please enter a word any length: ")
# word_third = input("Please enter a word any length: ")

# words = [word_one, word_second, word_third]
# longest_word = max(words, key=len)

# print(f"The longest word is: {longest_word}")
# print("The program is completed") 

""" Write a Python program to count the number of lines in a text file.
Matn faylidagi qatorlar sonini hisoblash uchun Python dasturini yozing."""

# def count_line(file_name): # created function 
#     try: #said try
#         with open(file_name, 'r') as file: #open my file with mode read
#             return len(file.read().splitlines()) 
#     except FileNotFoundError:
#         return "Error: File not found!" # if don't found my file show this message 


# file_name = "test.txt"  #Define the file name 
# print(count_line(file_name))

""""10. Write a Python program to count the frequency of words in a file.
Fayldagi so'zlarning chastotasini hisoblash uchun Python dasturini yozing."""
# from collections import Counter 

# def count_words(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read().lower() # hamma jarfalrni kichik harflarga o'tkazamiz
#             words = content.split() #contentni sozlarga bo'lib yuboramiz 
#             return Counter(words) 
#     except FileNotFoundError:
#         print("Oh ny God, File not found!")


# file_name = 'test.txt'  # Double quotes are not mandatory; single quotes can be used as well.
# print(count_words(file_name))

"""" 11. Write a Python program to get the file size of a plain file.
Oddiy faylning fayl hajmini olish uchun Python dasturini yozing."""
# import os  # fayl tizimi bilan ishlash uchun modul
# def get_file_size(file_name):
#     try:
#         size = os.path.getsize(file_name)  # fayl hajmini olish
#         return f"Fayl hajmi: {size} bayt"
#     except FileNotFoundError:
#         return "Xatolik: Fayl topilmadi!"
# file_name = "test.txt"
# print(get_file_size(file_name))

"""12.Write a Python program to write a list to a file.
Faylga ro'yxat yozish uchun Python dasturini yozing."""
# def write_list_to_file(file_name, data_list):
#     try:
#         with open(file_name, 'w') as file:
#             for i in data_list:
#                 file.write(str(i) + '\n')  # har bir elementni yangi qatordan yozadi
#         print("Ro'yxat muvaffaqiyatli yozildi!")
#     except Exception:
#         print("Xatolik yuz berdi")

 
# my_list = ["apple", "banana", "cherry", "grape"]
# file_name = "test.txt"

# write_list_to_file(file_name, my_list)

"""13. Write a Python program to copy the contents of a file to another file.
Fayl mazmunini boshqa faylga nusxalash uchun Python dasturini yozing."""

# def copy_file_contents(eski_file, yangi_file):
#     try:
#         with open(eski_file, 'r') as eski:
#             content = eski.read()
#         with open(yangi_file, 'w') as yangi:
#             yangi.write(content)
#         print("File contents copied successfully!")
#     except FileNotFoundError:
#         print("Error: Source file not found!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# eski_file = "test.txt"
# yangi_file = "fruits.txt"

# copy_file_contents(eski_file, yangi_file)

"""14. Birinchi fayldagi har bir satrni ikkinchi fayldagi tegishli qator bilan birlashtirish uchun Python dasturini yozing."""

# def merge_lines(file1, file2, output_file):
#     try:
#         with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
#             for line1, line2 in zip(f1, f2):
#                 out.write(line1.strip() + " " + line2.strip() + "\n")
#         print("Files merged successfully!")
#     except FileNotFoundError:
#         print("Error: One or more files not found!")
#     except Exception:
#         print("An error occurred")

# file1 = "test.txt"
# file2 = "fruits.txt"
# output_file = "merged_file.txt"

# merge_lines(file1, file2, output_file)

"""15. Write a Python program to read a random line from a file.
Fayldan tasodifiy qatorni o'qish uchun Python dasturini yozing."""

# import random
# def read_random_line(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#             if lines:
#                 return random.choice(lines).strip()
#             else:
#                 return "File is empty."
#     except FileNotFoundError:
#         return "Error: File not found!"

# file_name = "test.txt"
# print(read_random_line(file_name))

"""16. Write a Python program to assess if a file is closed or not."""

# def is_file_closed(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return file.closed  # Check if the file is closed inside the context manager
#     except FileNotFoundError:
#         return "Error: File not found!"

# file_name = "test.txt"
# print(f"Is the file closed? {is_file_closed(file_name)}")

"""17. Fayldan yangi qator belgilarini olib tashlash uchun Python dasturini yozing."""

# def clean_newlines(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#         with open(file_name, 'w') as file:
#             file.writelines(line.strip() + '\n' for line in lines)
#         print("Newline characters removed successfully!")
#     except FileNotFoundError:
#         print("Error: File not found!")

# file_name = "test.txt"
# clean_newlines(file_name)

"""18. Matn faylini kirish sifatida qabul qiladigan va berilgan matn faylidagi so'zlar sonini qaytaradigan Python dasturini yozing."""

def count_words_in_file(file_name):
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "Error: File not found!"

file_name = "test.txt"
print(f"The number of words in the file: {count_words_in_file(file_name)}")

"""19. Turli matnli fayllardan belgilar ajratib olish va ularni ro'yxatga qo'yish uchun Python dasturini yozing."""
def extract_characters_from_files(file_list):
    all_chars = []  # barcha belgilarni saqlovchi ro'yxat
    try:
        for file_name in file_list:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()        # faylni to‘liq o‘qish
                for char in content:
                    all_chars.append(char)   # har bir belgini ro‘yxatga qo‘shish
        return all_chars
    except FileNotFoundError:
        return "Xatolik: fayllardan biri topilmadi!"

# Sinov uchun:
files = ["file1.txt", "file2.txt", "file3.txt"]
characters = extract_characters_from_files(files)

print("Belgilar soni:", len(characters))
print("Birinchi 50 ta belgi:", characters[:50])


"""20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt."""
import string

def generate_files():
    for letter in string.ascii_uppercase:  # A dan Z gacha bo'lgan harflar
        file_name = f"{letter}.txt"
        with open(file_name, "w") as file:
            file.write(f"This is file {file_name}\n")
    print("✅ 26 ta fayl yaratildi!")

generate_files()

"""21. Ingliz alifbosining barcha harflari har bir satrda ma'lum miqdordagi harflar bilan ro'yxatga olingan fayl yaratish uchun Python dasturini yozing."""

def create_alphabet_file(file_name, letters_per_line):
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(0, len(alphabet), letters_per_line):
                file.write(alphabet[i:i+letters_per_line] + '\n')
        print(f"File '{file_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "alphabet.txt"
letters_per_line = 5  # Har bir satrda 5 ta harf
create_alphabet_file(file_name, letters_per_line)