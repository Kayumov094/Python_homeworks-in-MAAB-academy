print("Welcome to 2 repeat lesson")

# """1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age."""
# import datetime  # import datetime moduli 
# name = input("Please enter your name: ") # asked name from user 
# year = int(input("PLease enter your birth year: ")) #asked year of birth from user 
# today = datetime.datetime.today() # from datetime module called today date 
# print(today) # this is full date 
# current_year = today.year # called current year 
# print(f"Current year is {current_year}")
# print(f"Hello {name}, Your age is {current_year-year}. Congratulation!")

"""2. Extract car names from the following text:"""
# txt = 'LMaasleitbtui'
# txt_new = txt.split()
# #len() uzunlikni olchaydiga global function 
# txt_list = list(txt)
# print(txt_list[::2])
# car = []
# for i in txt_list[::2]:
#     car.append(i)

# print("".join(car))

"""3. Extract car names from the following text:"""
# txt = 'MsaatmiazD'
# txt_list = list(txt)
# car = []
# for i in txt_list[::2]:
#     car.append(i)

# print("".join(car))

"""4. Extract the residence area from the following text:"""
# txt = "I'am John. I am from London"
# area = txt.split()[-1]  # Extract the last word from the text
# print(area)

"""5. Write a Python program that takes a user input string and prints it in reverse order."""
# string = input("Please enter any word: ") # get any string
# print(string[::-1]) # printed reverse order

"""6.Write a Python program that counts the number of vowels in a given string. """
# print("Welcome to count Wovel programm")
# string = input("Please any word: ") # enter word from users 
# wovel = [] # create empty list 
# for i in string.lower():
#     if i in ("a", "u","e", "o", "i"):
#         wovel.append(i)

# print(f"Count of wovels {len(wovel)}") # print result 


"""7. Write a Python program that takes a list of numbers as input and prints the maximum value."""
# print("Welcome to find Maxsimum number programm")
# number_one = int(input("Please any first number: "))
# number_two = int(input("Please any second number: "))
# number_three = int(input("Please any third number: "))

# general_number =[number_one, number_two, number_three]
# print(f"Max number is {max(general_number)}, Congratulation!")

"""8. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward)."""
# names = ["level", "Civic", "Madam", "Noon"]
# check_polindrome = []
# for name in names:
#     if name.lower() == name.lower()[::-1]:
#         check_polindrome.append(name)

# print(check_polindrome)
    

"""9. Write a Python program that extracts and prints the domain from an email address provided by the user."""
# email = input("Please enter your email: ")
# domain = email.split(".")
# print(f"Your doamin is {domain[1]}, Congratulation!")

"""10. Write a Python program to generate a random password containing letters, digits, and special characters."""
# import random 
# import string
# print(string.ascii_lowercase) # string modulidagi barcha kichik harflar 
# print(string.ascii_uppercase) # string modulidagi barcha katta harflarni beradi
# print(string.digits) # ascii dagi barcha raqamlarni beradi
# print(string.punctuation) # ascii dagi barcha belgilarni chiqarib beradi
# print(string.ascii_letters) # barcha katta va kichik harflarni beradi
# print(string.printable)
# print(dir(string)) # string moduli ichidagi methodlarni chiqarib beradi
# characters = string.digits + string.ascii_letters + string.punctuation
# passwords = 12
# code = "".join(random.choice(characters) for _ in range(passwords))
# print(code)
 