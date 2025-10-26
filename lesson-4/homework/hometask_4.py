print("hello world")
""""1. Lug‘atni qiymat bo‘yicha tartiblang
Lug'atni qiymat bo'yicha saralash (o'sish va pasayish) uchun Python skriptini yozing."""

                # data = {"son1": 1, "son2": 2, "son3": 10, "son4": 5} #data nomli yangi lugat yaratib oldim
                # # Lug'atni qiymatlari bo'yicha o'sish tartibida saralash
                # new_dict = dict(sorted(data.items(), key=lambda item: item[1]))
                # print(new_dict)
                # print(data.items()) # data ichidagi barcha elementlarni chiqarib beradi
                # print(sorted(data.items(), key = lambda item: item[1])) # valuelardan kelib chqib tartiblaydi
                # print(sorted(data.items(), key = lambda item: item[0])) # keylardan kelib chiqib tartiblaydi


data = {"son1": 1, "son2": 2, "son3": 10, "son4": 5} #data nomli yangi lugat yaratib oldim
data_sorted = sorted(data.items(), key = lambda item: item[1]) # value lardan kelib chiqib tartiblaydi 
data_reversed = sorted(data.items(), key = lambda item: item[1], reverse = True) # value laardan kelib chiqib teskari tartiblaydi)
print(f"Tartiblangan lugat quyidagicha: {data_sorted}") # tartiblangan lugatni print qildim 
print(f"Teskari tartibda tartiblangan lug'at quyidagicha: {data_reversed}") # teskari tartiblangan lugatni print qildim 


# 2. Lug'atga kalit qo'shing
# Lug'atga kalit qo'shish uchun Python skriptini yozing.
data["son5"] = 25 # lugatga yangi key qo'shdim 
print(f"yangilanagan data {data}") # birinchi usul

data.update({"son6" : 30, "son7": 32}) # update() metodi oraqali yangiladim 
print(f"Yangilangan dict quyidagicha {data}") # yangilangan datani print qildim 

data1 = {"meva1": "olma", "meva2": "anor", "meva3": "banana"} # data1 nomli lugat yaratib oldim 
data2 = {"meva4": "kivi", "meva5": "shaftoli"} # data2 nomli yangi lugat yaratib oldim 
print(f"Ikkita dict ni birlashtirirdim {data1|data2}") # ikkita dictni birlashtirish orqali yangi dict hosil qildim 


new_data = {0: 10, 1: 20}
new_data[2] = 30 # berilgan dict ni yangiladim 
new_data.update({3:40}) #berilgan dictni ikkinchi usul bilan yangiladim
print(new_data)


# 3. Bir nechta lug‘atlarni birlashtiring
# Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun Python skriptini yozing.
dic1 = {1: 10, 2: 20} # namuna uchun dic1, dic2, dic3 berilgan 
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print(f"Dictlarni birlashtirish uchun {dic1|dic2|dic3}") #| yordamida to'plamlarni birlashtirdim 

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Dictionary (n = 5):

n = 5
new_dict = {x: x * x for x in range(1, n + 1)}  # for yordamida kvadratga oshirib oldim
print(new_dict) # new_dict ni chop etdim

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
k =15 # chegarani 15 deb beklgilab oldim
new = {x: x*x for x in range(1,k+1)} # har bir sonni k gacha teng bolguncha kvadratga oshirdim
print(new) # ozgaruvchini chop etdim

# 1. Create a Set
# Write a Python program to create a set.

new_set = {1,2,3,4,5,6} # new_set nomli yangi set yaratdim
print(type(new_set))

# 2. To‘plam ustida takrorlash
# To'plamlarni takrorlash uchun Python dasturini yozing.
new_set = {1,2,3,4,5,6} # new_set nomli yangi set yaratdim

for i in new_set: # set ichida aylanib chiqdim
    print(i)

# 3. To'plamga a'zo(lar)ni qo'shing
# To'plamga a'zo(lar)ni qo'shish uchun Python dasturini yozing.
new_set.add(7) # setga yangi element qo'shdim 
new_set.update([8,9,10]) # setga bir nechta elemntlarni qo'shdim 
print(new_set)


# 4. To'plamdan element(lar)ni olib tashlang
# Berilgan to'plamdan element(lar)ni olib tashlash uchun Python dasturini yozing.

new_set.remove(1) # remove orqali setdan elemtn olib tashladim 
 
new_set.discard(11) # discard bilan ochirish mumkin, lekin set ichida bolmasa ham xatolik qaytarmaydi 
new_set_popped = new_set.pop()
print(new_set_popped)
new_set. clear() # setni ichini tozalaydi lekin set o'zi qoladi

# 5. To'plamda mavjud bo'lsa, elementni olib tashlang
# Agar to'plamda mavjud bo'lsa, to'plamdan elementni olib tashlash uchun Python dasturini yozing.
new_set.remove(11) # agar remove da kiritilgan element set ichida bolmasa Keyerror qaytaradi
