print("Welcome to repeat lesson number 6")
"""1. Satr berilgan bo'lsa , har uchinchi belgidan keyin txtpastki chiziq ( ) qo'ying . 
_Agar belgi unli bo'lsa yoki undan keyin pastki chiziq bo'lsa, 
pastki chiziqni keyingi belgiga o'tkazing. Oxirida pastki chiziq qo'yilmasligi kerak.
Kirish: hello Chiqish: hel_lo

Kirish: assalom Chiqish: ass_alom

Kirish: abcabcabcdeabcdefabcdefg Chiqish: abc_abcab_cdeabcd_efabcdef_g"""

# def insert_underscore(xabar, n=3):
#     result = ""
#     count = 0

#     for char in xabar:
#         result += char
#         count +=1
#         if count == n:
#             result += "_"
#             count = 0
    
#     return result

# print(insert_underscore("hello"))
# print(insert_underscore("sdcswjcnsjncdncjdnjsdjjeeeoeoeooeoceo" , 4))
"""2. n Taqdim etilgan kod stubkasi STDIN dan butun sonni o'qiydi .
 Barcha manfiy bo'lmagan butun sonlar uchun i qaerda 0 <= i < n, chop eting i^2."""

# number  = int(input("Iltimos yigirmagacha bolgan son kitiring: "))
# if 1 <= number <= 20:
#     for i in list(range(number)):
#         print(i**2)
# else:
#     print("Iltimos 20 gacha son kiriting ")

"""LOOP ga asoslangan mashqalar 
 1-mashq: Birinchi 10 natural sonni while siklidan foydalanib chop eting"""
# n = 1
# while n < 10:
#     print(n)
#     n +=1


"""2. Quyidagi naqshni chop eting
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

# n = 1
# while n <= 5:
#     i = 1
#     line = ""
#     while i <= n:
#         line += str(i) + " "
#         i +=1
#     print(line.strip())
#     n +=1

"""3-mashq: 1 dan berilgan songacha bo‘lgan barcha sonlar yig‘indisini hisoblang"""
# i = 1
# n = int(input("Please enter number: "))
# while i <= n:
#      print(sum(list(range(i, n+1))))
#      break
 
"""4. Berilgan sonni ko‘paytirish jadvalini chop etish"""
# n = int(input("Please enter number: "))

# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1
   
"""5-mashq: Ro‘yxatdagi raqamlarni sikl yordamida ko‘rsatish.
numbers = [12, 75, 150, 180, 145, 525, 50]
75
150
145"""
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for number in numbers:
#     if number >= 75 and number <= 150:
#         print(f"{number}") 

"""6. 6-mashq: sondagi raqamlarning umumiy sonini hisoblang"""
# nums = 75869
# str_nums = str(nums)
# print(f"Raqamlarning umumiy soni {len(str_nums)}")
 
"""7-mashq: teskari raqamlar naqshini chop etish"""
# i = 5

# j =1
# # tashqi sikl satrlarni boshqaradi 
# # ichki sikl ichidagi sonlarni boshqaradi

# while i >= j:
#     j=i
#     while j >= 1:
#         print(j, end = " ")
#         j -= 1
#     print()
#     i -= 1

# a = 5
# b = 1
# while a >=1:
#     b = a
#     while b >=1:
#         print(b, end= " ")
#         b -= 1
#     print()
#     a -= 1 

# a = 1
 
# while a <= 10:
#     b = a
#     while b <= 10:
#         print(b, end = " ")
#         b += 1
#     print()
#     a += 1

# a = 1
# while a <= 10:
#     b = a
#     while b <= 10:
#         print(b, end=" ")
#         b += 1
#     print()  # yangi satrga o‘tadi
#     a += 1

"""8-mashq: Loop yordamida ro'yxatni teskari tartibda chop eting"""
# my_list = list(range(1, 10, 2))
# print(my_list)
# new = []
# for i in my_list:
#     new.append(i)
# print(list(reversed(new)))
 
"""9-mashq: for tsikli yordamida -10 dan -1 gacha raqamlarni ko'rsatish"""
# my_list = list(range(-10, 0,1))
# print(my_list)
# for i in my_list:
#     print(i)
 
"""Mashq 10: Muvaffaqiyatli tsikl bajarilgandan so'ng "Bajarildi" xabarini ko'rsatish"""
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done")

"""11-mashq: diapazondagi barcha tub sonlarni chop eting
Prime numbers between 25 and 50:"""

# for num in range(25, 50):
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")

"""12-mashq: Fibonachchi seriyasini 10 tagacha ko'rsating
0  1  1  2  3  5  8  13  21  34"""
# n = 10  
# a, b = 0, 1  
# print("Fibonachchi  elementlari:")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

"""13-mashq: Berilgan sonning faktorialini toping"""
# # 5! = 120
# import math 
# n = 5
# result = math.factorial(5)
# print(result)

"""Ikki ro'yxat o'rtasida umumiy bo'lmagan elementlarni qaytaring. Elementlarning tartibi muhim emas.
Kirish: list1 = [1, 1, 2], list2 = [2, 3, 4]
Chiqish: [1, 1, 3, 4]"""
# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]

# result = []

# for i in list1:
#     if i not in list2:
#         result.append(i)

# for j in list2:
#     if j not in list1:
#         result.append(j)

# print(result)
