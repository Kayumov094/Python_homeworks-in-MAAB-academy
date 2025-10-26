print("Hello world")
"""# Shunday dastur yozish kerakki
# Birinchi bo'lib birorta gap kiritishimiz lozim
# O'sha gap ichida qaysi so'z o'zgaradi va qaysi so'zga o'zgaradi
# Misol:
# Gapni kiriting: Men olmani yaxshi ko'raman
# Qaysi so'zni o'zgartirasiz: olma
# Qaysi so'zga almashtirasiz: limon
# Natija: Men limonni yaxshi ko'raman
# """
# print("Yangi dastur")
# gap = input("Biror gap kiriting: ")
# ozgaruvchi_soz = input("Bu gapingizda qaysi sozni o'zgartirmoqchisiz? ")
# yangi_soz = input("Yangi so'zni kiriting ")
# natija = gap.replace(ozgaruvchi_soz, yangi_soz)
# print("Natija:", natija)
# print("dastur tugadi")


# Yangi dastur yozamiz
print("Yangi dastur")
matn = input("Biror matn kiriting: ")
soz_sanash = len(list(matn.replace(" ", "")))
print("Siz kiritgan matnda", soz_sanash, "ta harf bor.")
print("dastur tugadi")