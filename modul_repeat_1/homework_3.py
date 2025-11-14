print("welcome to 3 repeat lesson")
"""1. Write a Python script to sort (ascending and descending) a dictionary by value."""
# flats = {1: "home", 2: "flat", 3: "house", 4: "dormitory"}
# sort() in-place va u list klassiga tegishli
# sorted() function bo'lib barcha iterable class ichida ishlaydi: list, set, tuple 
# sorted_keys = sorted(flats.keys()) # flars degan dict ning kalitlarini bo'yicha tartibladim 
# print(sorted_keys)

# print(dir(str))
# a = "asx"
# print(a.isprintable())

# b = "arslonek"
# print(b.partition("a"))
# data = "username=arslonek"
# key, sep, value = data.partition("=")
# print(key)   # username
# print(value) # arslonek
 
# print(dir(int))
# a = 5
# print(a.numerator)

# print(dir(float))
# print(oct(42))
# print(hex(42))
# print(dir(list))
# print(dir(tuple))
# print(dir(frozenset))
# print(dir(dict))
# print(dir(bool))
# x = None
# print(type(x))


"""1. Write a Python script to sort (ascending and descending) a dictionary by value."""
# my_dict = {7: "uy", 3: "meva", 4: "mashina"}
# # print(my_dict.items()) # barcha kalit-qiymat juftliklarini chiqaradi 
# # print(my_dict.keys()) # barcha kalitlarni chiqaradi
# # print(my_dict.get(4)) # get() ga kalit berish orqali chqirib olosh mumkin 
# # print(my_dict.values()) # qiymatlarini chaqirib olamiz 
# # # new_my_dict = sorted(my_dict.keys())
# # # print(new_my_dict)
# # print(my_dict)
# # new = sorted(my_dict)
# # print(new)
# # new_dict = {k: my_dict[k] for k in sorted(my_dict)}
# # print(new_dict)
# new_dict = {k: my_dict[k] for k in sorted(my_dict)} # list comprehension ishlatib toliq tartiblangan dictni olish mumkin 
# print(new_dict)

"""2. Write a Python script to add a key to a dictionary."""
# print(my_dict)
# my_dict[5] = "olma"  # Adding a new key-value pair to the dictionary
# print(my_dict)
# my_dict[8] = "hayvon" # yangi qiymat juftlik qo'shdim 
# print(my_dict)

"""3.Write a Python script to concatenate the following dictionaries to create a new one."""
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# dic1.update(dic2) # birinchi dic1 ga ikkinchi dicni qo'shdim 
# print(dic1)   
# dic1.update(dic3) # dic1 ga dic3 ni qo'shdim 
# print(dic1) # dic1 jamlangan dic1 hosil bo'ldi 

"""4.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary (n = 5):"""
# n = 5
# my_dict = {x: x * x for x in range(1, n + 1)}  # Dictionary comprehension to generate the required dictionary
# print(my_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# """5. Write a Python script to print a dictionary where the keys are numbers
#  between 1 and 15 (both included) and the values are the square of the keys."""
# n= 15
# my_new_dict = {x: x**2 for x in range(1, n+1)}
# print(my_new_dict)


"""6. Write a Python program to create a set."""
# my_list = list(range(10))
# print(my_list) # create list object 
# my_set = set(range(10))
# print(my_set) #create set object 

"""7. Write a Python program to iterate over sets."""
my_set = {1, 2, 3, 4, 5}
# for i in my_set: 
#     print(i)

"""8. Write a Python program to add member(s) to a set."""

# my_set.add(6)  # Adding a single member to the set
# print(my_set)

# my_set.update([7, 8, 9])  # Adding multiple members to the set
# print(my_set)

"""9. Write a Python program to remove item(s) from a given set."""

# print(my_set)
# my_set.remove(1) # 1 elementtini o'chirdim 
# print(my_set)
# my_set.discard(8) # 8 ni o'chirmoqchi lekin yoq. lekin xato qaytarmadi 
# print(my_set)

"""10. Write a Python program to remove an item from a set if it is present in the set."""

# print(my_set.pop())
# print(my_set)
 