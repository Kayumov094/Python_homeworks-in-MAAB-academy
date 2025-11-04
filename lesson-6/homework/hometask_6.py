print("Salom Arslonbek")
print("Oltinchi darsga xush kelibsiz!")
""" 1. Given a string txt, insert an underscore (_) after every third character. 
If a character is a vowel or already has an underscore after it, 
shift the underscore placement to the next character. No underscore should be added at the end.
Satr berilgan bo'lsa , har uchinchi belgidan keyin txtpastki chiziq ( ) qo'ying.
 _Agar belgi unli bo'lsa yoki undan keyin pastki chiziq bo'lsa, pastki chiziqni keyingi belgiga o'tkazing. Oxirida pastki chiziq qo'yilmasligi kerak.
Misollar
Kirish: hello Chiqish: hel_lo
Kirish: assalom Chiqish: ass_alom
Kirish: abcabcabcdeabcdefabcdefg Chiqish: abc_abcab_cdeabcd_efabcdef_g"""
# soz  = "name"
# print(soz.split("a"))
# print(soz.index("a"))
# print("-"join(["mike, john"]))
# print(dir(soz))
#  print(soz.insert(_,3))

# soz = input("Iltimos biror soz kiriting: ")
# son = "assalom"
# natija = ""
# for i in range(len(son)):
#     natija += son[i]
#     if (i+1)%3 == 0 and i !=len(son)-1:
#         natija += "_"
#     # elif son[(i+1)%3 == 0] in i
#         # natija += 1


        
# print(natija)

"""The provided code stub reads an integer, n, 
from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

Taqdim etilgan kod stubkasi nSTDIN dan butun sonni o'qiydi.
 Barcha manfiy bo'lmagan butun sonlar uchun iqaerda 0 <= i < n, chop eting i^2."""
# n = int(input(""))

# for i in range(n):
#     print(i * i)

"""1-mashq: Birinchi 10 natural sonni while siklidan foydalanib chop eting"""

# son = int(input("Iltimos biror son kiriting: ")) # foydalanuvchidan son qabul qilish
# i=1 # boshlang'ich qiymat
# while i <= son: # shart berdim 
#     print(i) # sonni chop etish
#     i += 1 # qiymatni oshirish

"""2-mashq: Quyidagi naqshni chop eting"""
# n = 5

# for i in range(1, n+1): # tashqi sikl yaratdim 
#     for j in range(1, i+1): # ichki sikl yaratdim
#         print(j, end=" ") # j ni chop etish
#     print()# yangi qatorga o'tish

"""3-mashq: 1 dan berilgan songacha bo‘lgan barcha sonlar yig‘indisini hisoblang"""
# n = 10 # 10 soni berilgan shunio summasini topish kerak
# summa = 0 # yig'indini saqlash uchun o'zgaruvchi yaratdim
# for i in range (1, n+1): # 1 dan n gacha bo'lgan sonlar uchun
#     summa += i # yig'indini hisoblash
# print("Yig'indi:", summa)  # natijani chop etish

"""4-mashq: Berilgan sonni ko‘paytirish jadvalini chop etish"""
# n = 2 # ko'paytirish jadvalini chiqarish kerak bo'lgan son
# for i in range(1, 11): # 1 dan 10 gacha
#     print(f"{n * i}") # ko'paytirish jadvalini chop etish
     
"""5-mashq: Ro‘yxatdagi raqamlarni sikl yordamida ko‘rsatish"""
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for number in numbers:
#     if number > 500:
#         break
#     elif number >150:
#         continue
#     elif number % 5 == 0:
#         print(number)

"""6-mashq: sondagi raqamlarning umumiy sonini hisoblang"""
# n = 75869 # berilgan son
# count = 0
# while n > 0:      # son tugamaguncha
#     n //= 10      # sonni 10 ga bo‘lib, oxirgi raqamni olib tashlaymiz
#     count += 1       # raqamlar sanog‘ini oshiramiz
# print(count)

"""7-mashq: teskari raqamlar naqshini chop etish"""
# n = 5
# for i in range(n, 0, -1):  # 5 dan 1 gacha kamayadi
#     for j in range(i, 0, -1):    # i dan 1 gacha kamayadi
#         print(j, end=" ")
#     print()
"""8-mashq: Loop yordamida ro'yxatni teskari tartibda chop eting"""

# list1 = [10, 20, 30, 40, 50]

# for i in range(len(list1)-1, -1, -1):
#     print(list1[i])   

"""9-mashq: for tsikli yordamida -10 dan -1 gacha raqamlarni ko'rsatish"""
# for i in range(-10, 0):
#     print(i)

"""Mashq 10: Muvaffaqiyatli tsikl bajarilgandan so'ng "Bajarildi" xabarini ko'rsatish"""
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

"""11-mashq: diapazondagi barcha tub sonlarni chop eting"""
 
# start = 25
# end = 50

# print("Prime numbers between", start, "and", end, ":")

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
"""12-mashq: Fibonachchi seriyasini 10 tagacha ko'rsating"""
# n = 10  
# a, b = 0, 1  
# print("Fibonachchi  elementlari:")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
"""13-mashq: Berilgan sonning faktorialini toping"""
# n = 5  # berilgan son
# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(f"{n}! = {factorial}")
"""4. Ro'yxatlarning noodatiy elementlarini qaytaring"""
def umumiy_elementlar(list1, list2):
    natija = []
    # list1 elementlari, list2 da yo'q bo'lganlari
    for x in list1:
        if x not in list2:
            natija.append(x)
    # list2 elementlari, list1 da yo'q bo'lganlari
    for x in list2:
        if x not in list1:
            natija.append(x)
    return natija

 
print(umumiy_elementlar([1, 1, 2], [2, 3, 4]))        # [1, 1, 3, 4]
print(umumiy_elementlar([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]
print(umumiy_elementlar([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
