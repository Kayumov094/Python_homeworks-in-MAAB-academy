# my_list = [12, 8, 3, 13, 8, 7]

# #  natija : juft sonlar yigindisi = 28, toq sonlar yigindisi = 23
# juft_sonlar = 0
# toq_sonlar = 0
# while my_list:
#     son = my_list.pop()
#     if son%2 ==0:
#         juft_sonlar += son
#     else:
#         toq_sonlar += son
# print(f"Juft sonlar yg'indosi = {juft_sonlar}, Toq sonlar yigindisi {toq_sonlar}")

"""Shunday bir funksiya yaratish kerak, u ishga tushganda userdan ikkita sonni qabul qilsin
va 1-son 2-sonning nechi foizini tashkil qilishini menga return qilishi lozim."""
son1 = int(input("Iltimos birinchi sonni kirit: "))
son2 = int(input("Iltimos ikkinchi sonni kirit: "))
def foizni_hisobla(son1, son2):
    natija = (son1/son2)*100
    return natija

print(foizni_hisobla(son1, son2))

