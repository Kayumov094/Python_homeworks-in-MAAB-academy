"""my_list = ['Adam Smith', 'Ernst Thompson', 'Agatha Christie', 'Paul Jhons']
#  Topshiriq: 4 ta so'zning uzunligidan iborat bo'lgan boshqa bir list yaratish
result = [10, 14, 15, 10]"""

# my_list = ['Adam Smith', 'Ernst Thompson', 'Agatha Christie', 'Paul Jhons']
# new_list = []

# for name in my_list:
#     new_list.append(len(name))

# print(new_list)

# my_list = ['Adam Smith', 'Ernst Thompson', 'Agatha Christie', 'Paul Jhons']

# i=0
# while i < len(my_list):
#     print(len(my_list[i]))
#     i = i + 1


# my_list = [12, 7, 54, 33, 90]
# juft_sonlar = []
# toq_sonlar = []
# for number in my_list:
#     if number % 2 == 0:
#         juft_sonlar.append(number)
#     else:
#         toq_sonlar.append(number)

# print("Juft sonlar:", juft_sonlar, "Toq sonlar:", toq_sonlar)
 
# while True:
#     user_input = input("O'yinni toxtatishni xohlaysizmi? ")
#     if user_input.lower() == "ha" or user_input.lower() == "albatta":
#         print("O'yin toxtatildi")
#     elif user_input.lower() == "albatta":
#         print("O'yin toxratildi")
#     break
 
my_list = ['Adam Smith', 'Ernst Thompson', 'Agatha Christie', 'Paul Jhons']

for name in my_list:
    print(f" Men qidirayotgan ism {name} va unda {name.count("a")} ta a harfi bor ekan")

#         print(name.pop("a").count())
# print("Vazifa Bajarildi")