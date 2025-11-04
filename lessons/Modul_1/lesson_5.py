# print("Hello wolrd")
# True == 1
# print(id(None))
# print(type(None))
# # print(value(None))
"""Agar imtixon baxosi 
manfiy kiritsa baxo manfiy bo'lishi mumkin emas deb chiqsin
0 va 30 orasida bo'lsa sizda shartmandali holat deb chiqsin
30 va 60 orasida bo'lsa qattiqroq ishlishingiz lozim deb chiqsin
60 va 80 orasida bo'lsa qoniqarli
80 va 90 orasida bo'lsa yaxshi
90dan baland bo'lsa a'lo
100 dan oshib ketsa o'zi maksimum ball 100 deb chiqsin
# """

# baho = int(input("Iltimos imtixon bahoingizni kiriting: "))
# if baho < 0:
#     print("Baho manfiy bo'lishi mumkin emas")
# elif baho > 0 and baho < 30:
#     print("Sizda sharmandali holat")
# elif baho >=30 and baho <60:
#     print("Qattiqroq ishlashingiz lozim")
# elif baho >=60 and baho <80:
#     print("Qoniqarli")
# elif baho >=80 and baho <90:
#     print("Yaxshi")
# elif baho >=90 and baho <=100:
#     print("A'lo")
# else:
#     print("O'zi maksimum ball 100")
"""
# txt, csv, tsv - flat file
# jpg, png, mp4, mp3 - media file
# py, js, cpp, java - programming file


Userdan tòliq fayl nomi sòralsin
Agar òsha fayl nomi tepadagilardan biri bilan tugasa Siz kiritgan fayl - shu turdagi fayl deb chiqsin
For e:
User : news.txt
Output Siz kiritgan fayl flat file
"""
# file_name = input("Iltimos fileni  kiriting: ")
# if file_name.endswith(".txt") or file_name.endswith(".csv") or file_name.endswith(".tsv"):
#     print("Siz kiritgan fayl - flat file")
# elif file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".mp4") or file_name.endswith(".mp3"):
#     print("Siz kiritgan fayl - media file")
# elif file_name.endswith(".py") or file_name.endswith(".js") or file_name.endswith(".cpp") or file_name.endswith(".java"):
#     print("Siz kiritgan fayl - programming file")   
# else:
#     print("Siz kiritgan file - Noma'lum fayl turi")


# file_name = input("Iltimos fileni nomini kiriting: ")
# if file_name.endswith((".txt", ".csv", ".tsv")): 
#     print("Siz kiritgan fayl - flat file")
# elif file_name.endswith((".jpg", ".png", ".mp4", ".mp3")):
#     print("Siz kiritgan fayl - media file")
# elif file_name.endswith((".py", ".js",".cpp",".java")):
#     print("Siz kiritgan fayl - programming file")   
# else:
#     print("Siz kiritgan file - Noma'lum fayl turi")


# a = 10
# b = 10
# print(id(a), id(b))
# print(a == b)
# print(a is b)

# prev_num = 0
# for i in my_list:
#     print(i + prev_num)
#     prev_num = i
# min_num = 0
# max_num = 0
# my_list = [12, 89, 45, 34, 9, 67]
# min_num = my_list[0]

# for i in my_list:
#     if i < min_num:
#     #    print(f"Bu yerda min_num {min_num} ekan")
#        min_num = i

# print(min_num)
    
my_list = [12, 89, 45, 34, 9, 67]

max_num = my_list[0]
for i in my_list:
    if i> max_num:
        max_num = i

print(max_num)