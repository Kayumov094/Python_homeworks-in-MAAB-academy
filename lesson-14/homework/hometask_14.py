print("Welcome to homework 14")
import requests
import random
import json
"""write a Python script that reads the students.jon JSON file and prints details of each student.
"""
 

students = """
{
    "talabalar":[
        {
            "name": "Ali Valiyev",
            "age": 20,
            "courses": ["Matematika", "Fizika"]
        },
        {
            "name": "Sara Karimova",
            "age": 22,
            "courses": ["Biologiya", "Kimyo"]
        },
        {
            "name": "Olimjon Tursunov",
            "age": 19,
            "courses": ["Informatika", "Matematika"]
        }
    ]
}
"""
# print(json.loads(students)) # JSON str ni Python objectga aylantirdim (dict)

# student_dict = json.loads(students) # python objectini student_dict degan ozgaruvchiga tenglab oldim 

# stident.json degan file ochib unga student_dict ni json formatida yozdim 
# with open('students.json', 'w') as file:
#     json.dump(student_dict, file, indent = 4)

# endi shu students.json degan file ochib o'qiymiz 
with open('F:\Arslonbek\MySecondBrain\DataAnalitika\Python_homework\lesson-14\homework\students.json') as file:
    students_data = json.load(file) # file dan o'qilgan json formatini python obyektiga aylantirdim 

for student in students_data['talabalar']:
    print(f"name student: {student['name']},\n"
          f"age student: {student['age']},\n"
          f"cources of student: {', '.join(student['courses'])}\n") 
 


"""Ushbu urldan foydalaning: https://openweathermap.org/
Muayyan shahar (masalan, siz tug'ilgan shahar: Toshkent) uchun ob-havo ma'lumotlarini olish 
va tegishli ma'lumotlarni (harorat, namlik va boshqalar) chop etish uchun so'rovlar kutubxonasidan foydalaning."""
 
# city = "Tashkent" #
# api_key = "cc34911a108a2187a6183befa646264f"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# response = requests.get(url)
# print(f"Status code: {response.status_code}")
# data = response.json()
# print(data)
# print(json.dumps(data, indent = 8))
# wind = data['wind']['speed']
# temperature = data['main']['temp']
# humidity = data['main']['humidity']
# print(f"Current temp in Tashkent: {temperature}°C")
# print(f"current humidity in Tashkent: {humidity}%")       
# print(f"current wind speed in Tashkent: {wind} m/s")




"""Foydalanuvchilarga yangi kitoblar qoʻshish, 
mavjud kitob maʼlumotlarini yangilash va books.json JSON faylidan kitoblarni 
oʻchirish imkonini beruvchi dastur yozing."""
 
# data = """
# {
#     "books" : [
#         {
#             "title": "Python Basics",
#             "author": "John Doe",
#             "year": 2021,
#             "genres": ["Programming", "Education"]
#         },
#         {
#             "title": "Data Science Handbook",
#             "author": "Jane Smith",
#             "year": 2020,
#             "genres": ["Data Science", "Machine Learning"]
#         }
#     ]
# }
# """
# with open('books.json', 'w') as file: 
#     json.dump(data, file, indent = 4) # Python objectni JSON file ga saqladim

# with open('books.json') as file:
#     my_data = json.load(file)

# print(json.loads(data))
# book = {
#     "title": "Python Basics",
#     "author": "John Doe",
#     "year": 2021,
#     "genres": ["Programming", "Education"]
# }
# my_data = json.dumps(book, indent = 4)
# print(book['genres'][1])

"""Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre.
"""
 

# genre = input("Please enter genre movie: ")
 
# url = f"http://www.omdbapi.com/?i=tt3896198&apikey=fd9b27c6&s={genre}"
 
# response = requests.get(url)
# data = response.json()
# #JSON ni chiroyli chiqirishning birinchi usuli 
# # print(json.dumps(data, indent = 4))

# # JSON objectni chiroyli chiqarishnining birinchi usuli 
# # from pprint import pprint
# # pprint(data)

# # print(json.dumps(data, indent = 4, ensure_ascii = False))
# movies = data['Search']
# # print(movies)
# random_movie = random.choice(movies)
# print(f"Siz uchun tavsiya etilgan kino: {random_movie['Title']} ({random_movie['Year']})")