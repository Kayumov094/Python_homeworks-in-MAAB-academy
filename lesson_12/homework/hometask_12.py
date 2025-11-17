print("Arslonbek Welcome to 12 lesson")
# threads bu dastur ichida bir nechta oqim hosil qilib beradi
import threading # threading modulini chiqarib oldim 
import time # time modulini chqaririb oldim 

# def hello(): # hello funksiyasi yaratib oldim 
#     print("Hello") # hello ni print qil
#     time.sleep(3) # 3 soniyada kodmi ishga tushir 

# def world():
#     print("world")
#     time.sleep(5) # dasturni 5 soniyada ishga tushir deb belgiladim 

# #thread yarataman 
# t1 = threading.Thread(target = hello) # threading modulidan Thread funksiyasini chaqirib helloga tenglayapman
# t2 = threading.Thread(target = world) # threading modulidan Thread funksiyasini chaqirib world ga tenglayapman

# ## thread larni ishga tushirish start() bilan bajariladi 
# t1.start() # birinchi ipni ishga tushuryapman 
# t2.start() # ikkinchi oqimni ishga tushiryapman 

# # thread lar tugashini kutish 
# t1.join() # birinchi oqim tugashini kutaman 
# t2.join() # ikkinchi oqim tugashini kutaman 


# def mission(a: int):
#     time.sleep(5)
#     print(f" Sonning kvadrati: {a**2}")

# t1 = threading.Thread(target = mission, args=(3,))
# t1.start()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

import threading

primes = []          # barcha tub sonlar bu yerga yoziladi
lock = threading.Lock()

def check_primes(start, end):
    for n in range(start, end+1):
        if is_prime(n):
            with lock:           # ro'yxatga xavfsiz qo'shish
                primes.append(n)

start = 1
end = 100
num_threads = 4

# Threadlarga diapazonni taqsimlash
step = (end - start + 1) // num_threads
threads = []

for i in range(num_threads):
    s = start + i*step
    e = start + (i+1)*step - 1 if i != num_threads-1 else end
    t = threading.Thread(target=check_primes, args=(s, e))
    threads.append(t)
    t.start()

# Barcha threadlar tugashini kutish
for t in threads:
    t.join()

primes.sort()  # tartiblash
print("Tub sonlar:", primes)


 

import threading
from collections import Counter

file_path = "katta_matn.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

num_threads = 4
step = len(lines) // num_threads

lock = threading.Lock()
results = []

def count_words(lines_chunk):
    counter = Counter()
    for line in lines_chunk:
        words = line.strip().split()
        counter.update(words)
    with lock:
        results.append(counter)

threads = []
for i in range(num_threads):
    start = i * step
    end = (i+1)*step if i != num_threads-1 else len(lines)
    t = threading.Thread(target=count_words, args=(lines[start:end],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_counter = Counter()
for c in results:
    final_counter.update(c)

print("Top 10 eng ko'p ishlatilgan so'zlar:")
print(final_counter.most_common(10))
