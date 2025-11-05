print("Salom Arslonbek")
print("Yettinchi darsga xush kelibsiz")
"""1-task 
map Funksiyalar va funktsiyalar haqida bilib oling filter va ularni sinfda tushuntirishga tayyor bo'ling. 
Ushbu funktsiyalardan iboralar yordamida misollar keltiring lambda.
"""
# map() royhatdagi harbir elementga bitta funksiyani qo'llaydi va natijalarni yangi royhatda qaytaradi.
# filter() royhtadgi elementlarga bitta funksiyani qo'llaydi va faqatgina True qiymat qaytargan elementlarni yangi royhatda qaytaradi.
#Lambda funksiyasi  - kichik anonim funksiyalar yaratish uchun ishlatiladi.
#misol map funksiyasi
my_list = [1, 2, 3 ,4, 5]
def kvadrat(x):
    return x**2
natija = list(map(kvadrat, my_list))
print(natija)
print(map(kvadrat, my_list)) # iterable obect qytaradi 
print(list(map(kvadrat,my_list))) #iterable objectni listga aylantirib visibility qiladi

#filter() example
my_list = [10, 25 , 35, 40]
def toq_sonlar(x):
    return x%2 == 0

natija = list(filter(toq_sonlar, my_list))
print(natija) #

"""is_prime(n)funksiyasini hosil qiling ( n > 0). Agar nsoni tub bo'lsa True, aks holda Falseqiymat qaytarsin."""
def is_prime(n):
    while n< 0:
        return "Iltimos musbat son kiriting"
    if n < 2:
        return f"{n} bu son tub emas"
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return f"Bu {n} soni tub son ekan"

print(is_prime(7))
print(is_prime(31))
print(is_prime(1))

"""digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi."""
def digit_sum(k): #functionni define qildim 
    return sum(int(d) for d in str(k)) # string sifatida har bir k uchun raqam d deb hisoblab qaytar

print(digit_sum(24)) # sonlarni hisoblovchi funksiyani print qildim 
print(digit_sum(502)) # sonlarni hisoblovchi funksiyani print qildim 
 
"""Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini 
 (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing."""
def darajaga_oshir(n): # function ni elon qildim
    if n < 0:
        return f"Iltimos musbat son kiriting"
    
    k =  1 
    natija = []
    while 2**k < n: #qachonki 2 ni darajasi  n dan kichik ekan
        natija.append(2**k) # natija degan listga 2**k ni append qil dedim 
        k +=1
    return natija

print(darajaga_oshir(10)) # funksiyani ishga tushirdim 