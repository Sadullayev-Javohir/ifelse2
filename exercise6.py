"""To'lov usuli matn shaklida kiritiladi naqd yoki kartada. Agar naqd deb kiritilsa
summa kiritishni so'raydi agar karta deb kiritilsa parol kiriting deb so'rasin"""

pay = input("naqd yoki karta kiriting: ")

if pay.capitalize() == "naqd".capitalize():
    summa = int(input("Summa kiriting: "))
    if summa > 0 or summa < 0:
        print(f"Sizning summangiz: {summa}")
elif pay.capitalize() == "karta".capitalize():
    karta = input("Parol kiriting: ")
    if len(karta) > 0:
        print(f"Sizning parolingiz: {karta}")
else:
    print(f"{pay} ? karta yoki naqd kiriting. ")