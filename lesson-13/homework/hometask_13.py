print("Welcome to 13 rd  lesson")
"""1. Age Calculator: Ask the user to enter their birthdate. 
Calculate and print their age in years, months, and days."""
 
# yosh  = int(input("Tugilgan kuningizni kiriting: "))
# oy = int(input("Tugilgan oyingizni kiriting: "))
# yil = int(input("Tug'ilgan yilingizni kiriting: "))

# from datetime import date 
# def yosh_hisoblash():
#     bugun = date.today()
#     # print(bugun)
#     yosh_yil = bugun.year - yil
#     yosh_oy = bugun.month - oy
#     yosh_kun = bugun.day - yosh
#     if yosh_oy < 0:
#         yosh_yil -= 1
#         yosh_oy += 12
#     if yosh_kun < 0:
#         yosh_oy -= 1
#         yosh_kun += 30
#     print(f"Sizning yoshingiz: {yosh_yil} yil, {yosh_oy} oy, {yosh_kun} kun")

# print(yosh_hisoblash())

"""2. Days Until Next Birthday: Similar to the first exercise, 
but this time, calculate and print the number of days remaining until the user's next birthday."""
"""Keyingi tug'ilgan kungacha bo'lgan kunlar: Birinchi mashqga o'xshash, 
ammo bu safar foydalanuvchining keyingi tug'ilgan kuniga qadar qolgan kunlar sonini hisoblang va chop eting.
"""
# from datetime import date, datetime

 
# tugilgan_kun = input("tugilgan kuningizni kiriting (YYYY - MM -DD): ")
# tugilgan_kun_date = datetime.strptime(tugilgan_kun, "%Y-%m-%d") # bu str ni datetime formatiga aylantiradi vaqtlari bilan chiqaradi  
# tugilgan_kun_date = datetime.strptime(tugilgan_kun, "%Y-%m-%d").date() #  datetime formatini faqat kunlarini chiqaradi 
# bugun = date.today()
# print(bugun)
# keyingi_tugilgan_kun = tugilgan_kun_date.replace(year = bugun.year)
# if keyingi_tugilgan_kun < bugun:
#     keyingi_tugilgan_kun = keyingi_tugilgan_kun.replace(year = bugun.year + 1)
#     qolgan_kunlar = (keyingi_tugilgan_kun - bugun).days
#     print(f"Sizning keyingi tugilgan kuningizgacha {qolgan_kunlar} kunlar qoldi.")
 
# print(tugilgan_kun_date)


""""3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration
 of a meeting in hours and minutes. 
Calculate and print the date and time when the meeting will end.."""
 

# from datetime import datetime, timedelta # datetime va timedelta modulini import qilib oldim
# joriy_sana_va_vaqt = input("Please enter the current date and time (YYYY-MM-DD HH:MM): ") # userdan joriy sana vaqtni kiritishni soradim
# joriy_sana_va_vaqt_td = datetime.strptime(joriy_sana_va_vaqt, "%Y-%m-%d %H:%M") # vaqtni datetime formatiga aylantirib oldim 
# uchrashuv_davomiyligi = input("Please enter the duration of the meeting (hours minutes): ") # userdan uchrashuuv davimiylagini soradim 
# soat, daqiqa = map(int, uchrashuv_davomiyligi.split()) # soat va daqiqa degan o'zagruvchi yaratib daviylikni split() qildim 
# timedelta_td = timedelta(hours = soat, minutes = daqiqa)  # timedelt_td degan o'zgaruvchini timedelta orqali yartib oldim 
# uchrashuv_vaqti_tugashi = joriy_sana_va_vaqt_td + timedelta_td # joriy vaqtga uchtrashuv davomiyligini kiritdim 
# print(f"The meeting will end on: {uchrashuv_vaqti_tugashi.strftime("%Y-%m-%d %H:%M")}") # resuktni string formatda print qildim


"""4. Timezone Converter: Create a program that allows the user to enter a date and time 
along with their current timezone, 
and then convert and print the date and time in another timezone of their choice."""
 
# print("timezone daturi")
# from datetime import datetime
# import pytz
# joriy_sana_va_vaqt = input("Please enter the current date and time (YYYY-MM-DD HH:MM): ")
# joriy_vaqt_mintaqasi = input("Please enter your current timezone ('Asia/Japan'): ")
# joriy_sana_va_vaqt_td = datetime.strptime(joriy_sana_va_vaqt, "%Y-%m-%d %H:%M")
# print(joriy_sana_va_vaqt_td)  # datetime formatida chiqaradi
# joriy_vaqt_mintaqasi_td = pytz.timezone(joriy_vaqt_mintaqasi)
# print(joriy_vaqt_mintaqasi_td) # timezone formatida chiqaradi
# joriy_sana_va_vaqt_td = joriy_vaqt_mintaqasi_td.localize(joriy_sana_va_vaqt_td)
# print(joriy_sana_va_vaqt_td)
 

"""5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, 
and then continuously print the time remaining until that point in regular intervals (e.g., every second)."""

 
# kelajak_vaqt = input("Please enter a future date and time DD/MM/YYYY HH/MM): ")
# from datetime import datetime, timedelta # datetime va timedelta modullarini import qildim 
# import time # time modulini import qildim 
# import pytz # pytz modulini import qildim 
# kelajak_vaqt_td = datetime.strptime(kelajak_vaqt, "%d/%m/%Y %H/%M") # kiritilgan vaqtni datetime formatiga aylantirib oldim 
# print(kelajak_vaqt_td) # tayyor datetime ni print qiildim 
# bugun =datetime.now() # bugun degan o'garuvchiga datetime dagi hozirgi vaqtni yukladim 
# print(f"bugun: {bugun}") # bugun degan ozgaruvchini print qildim 
# while kelajak_vaqt_td > bugun: # qachonki kelajak_vaqt bugundan kichik ekan
#     qolgan_vaqt = kelajak_vaqt_td - bugun #kelajak_vaqtdan hozirgi vaqtni ayirdim 
#     print(f"Qolgan vaqt: {qolgan_vaqt}") # qolgan vaqtni print qildim 
#     time.sleep(1) # 1 soniya kuti turadi 
#     bugun = datetime.now() # 1 sonidan keyin chiqargandan keyin bugun yangilanadi
# print("Time close!")


"""6. Email Validator: Write a program that validates email addresses. 
Ask the user to input an email address, and check if it follows a valid email format."""
 
# import re # regular expression modulini import qildim 
# email_manzil = input("Please enter your email address: ") #arslonbekqayumov094@gmail.com
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.match(pattern, email_manzil):
#    print("Valid this email address.")
# else:
#     print("Invalid this email address.")

# import re 
# email_manzil = input("Please enter your mail address: ")
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.match(pattern, email_manzil):
#     print("Valid this email")
# else:
#     print("Invalid this email")

"""7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format.
 For example, convert "1234567890" to "(123) 456-7890"."""
"""Telefon raqamini formatlovchi: telefon raqamini kiritish sifatida qabul qiladigan 
va uni standart formatga muvofiq formatlaydigan dastur yarating. 
Masalan, "1234567890" ni "(123) 456-7890" ga aylantiring."""
# import re 
# print("Phone number formatter")
# phone_number = input("Please enter your phone_number (+99890-577-35-23): ")
# pattern = r'^\+998(\d{2})-(\d{3})-(\d{2})-(\d{2})$'
# if re.match(pattern, phone_number):
#     formatted_number = re.sub(pattern, r'(\1) \2-\3-\4', phone_number)
#     print(f"Formatted phone number: {formatted_number}")

import re 
 
# phone_number = input("Enter phone number please:(+998905773523) ")
# pattern = r'^\+998(\d{2})(\d{3})(\d{2})(\d{2})$'
# if re.match(pattern, phone_number):
#     formatted_number = re.sub(pattern, r'((((\1)))) \2\*\3\*\4', phone_number)
#     print(f"Formatted phone_number: {formatted_number}")
# else:
#     print("Invalid phone number")
"""8. Password Strength Checker: Implement a password strength checker. 
Ask the user to input a password and check if it meets certain criteria 
(e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit)."""

 

# parol = input("Please enter your password: ")
# if (len(parol)) >= 8 and re.search(r'[A-Z]', parol) and re.search(r'[a-z]', parol) and re.search(r'[0-9]', parol):
#     print("This password is very strong")
# else:
#     print("This password is weak")

"""9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
"""

"""9.Word Finder: Berilgan matnda ma'lum bir so'zning barcha ko'rinishlarini topadigan dastur ishlab chiqing.
 Foydalanuvchidan so'z kiritishni so'rang, 
so'ngra namuna matnida ushbu so'zning barcha uchraydigan joylarini qidiring va chop eting.
 """
# word = input("Please enter any wordflow: ")
# sample_text = """Nowadays, I am learning Ptyhon programming language. Python is very popular and versatile."""
# pattern = rf'\b{re.escape(word)}\b'
# matches = re.findall(pattern, sample_text, re.IGNORECASE)
# if matches:
#     print(f"The word '{word}' found {len(matches)} times in the sample text.")
# else:
#     print(f"The word '{word}' not found in the sample text.")

# word = input("PLease enter any words: ")
# sample_text = """Nowadays, I am learning Python programming language. Python is very popular and versatile."""
# pattern = rf'\b{re.escape(word)}\b'
# if re.findall(pattern, sample_text, re.IGNORECASE):
#     print(f"Bu '{word}' sozi topildi")
# else:
#     print(f"Bu '{word}' sozi topilmadi")

"""10. Date Extractor: Write a program that extracts dates from a given text.
 Ask the user to input a text, and then identify and print all the dates present in the text."""

"""10. Sana Extractor: Berilgan matndan sanalarni ajratib oluvchi dastur tuzing.
 Foydalanuvchidan matn kiritishni so'rang, so'ngra matndagi barcha sanalarni aniqlang va chop eting.
"""
matn = input("Please any words: ")
pattern = r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'
dates = re.findall(pattern, matn)
if dates:
    print("Ajratib olinganlar:")
    for date in dates:
        print(date)