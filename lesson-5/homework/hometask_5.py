print("Hello world")
print("Beshinchi darsga xush kelibsiz!")

""" 1.Berilgan yil kabisa yili ekanligini aniqlaydi."""

yil = int(input("Kabisa ekanligini tekshirish uchun yilni kiriting: "))
def kabisami(yil):
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        return f"Siz kiritgan {yil} yili kabisa yili hisoblanadi."
    else:
        return f"Siz kiritgan {yil} tili kabisa yili emas! Uzr."
    
print(kabisami(yil))

"""2. Conditional Statements Exercise"""
# n = int(input("Iltimos biror sonni kiriting: "))

def Shartni_tekshir(n): # shartni tekshir degan function elon qildim
    if not isinstance(n, int): # sonni butunligini tekshirib oldim 
        return "Iltimos Faqat butun son kiriting!" # agar shart bajarilmasa bu xabar qaytadi
    if not ( 1 < n < 100): # sonni 1 dan 100 gacha oraligda bolsin degan shart kiritdim
        return "Iltimos 1 dan 100 gacha bo'lgan sonlarni kiriting!"  # agar shart bajarilmasa bu xabar qaytadi
    if n % 2 != 0: # agar son toq bolsa 
        return "Weird" # bu xabar qaytaradi
    elif n % 2 != 0 and 1< n < 6: # agar son ham toq ham 1 dan 5 gacha oraliqqa tushsa 
        return "Not Weird" # bu xabar qaytariladi
    elif n % 2 == 0 and 6 < n < 20: # agar son juft va 6 va 20 gacha oraliqqa tushsa 
        return "Weird" # buu xabar qaytariladi
    elif n % 2 == 0 and n > 20: # agar son juft va 20 dan katta bolsa 
        return "Not Weird" #bu xabar qaytariladi
    
print(Shartni_tekshir(3)) # funksiyamizni tekshirib koramiz 

"""3. Input Format. A single line containing a positive integer, n.
A va b ikkita butun son berilgan. Bu raqamlar orasidagi juft sonlarni toping. a va b o'z ichiga oladi. 
Loop ishlatmang.
Ikkita yechim bering. 
1-yechim if-else ifodasi bilan.
2-yechim if-else ifodasisiz."""
a = int(input("Iltimos birinchi butun son kiriting: "))
b = int(input("Iltimos ikkinchi butun sonni kiriting: "))
def juft_sonlar(a, b):
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    return list(range(a, b+1, 2))

son = juft_sonlar(a, b)
print(son)

# 2 variant

a = int(input("Iltimos birinchi sonni kiriting: ")) # birinchi sonni kiritishini soradim
b = int(input("Iltimos ikkinchi sonni kiriting: ")) # ikkinchi sonni kiritishini soradim

def juft_sonlar_2(a, b): # juft_sonlar_2 degan function elon qildim
    start = a + (a%2) # agar a soni toq bolsa unga 1 ni qoshib start degan o'zagruvchiga saqlaydi
    end = b + 1 - (b%2) # agar b soni toq bolsa undan 1 ayirib end degan o'zgaruvchiga saqlaydi
    return list(range(start, end, 2)) # natijada start bilan end orasidagi butun sonlar royhatini qaytaradi

sonlar = juft_sonlar_2(a,b) # funksiyani chaqirib sonlar degan o'zgaruvchiga saqlaymiz
print(sonlar) # natijani chop etamiz


