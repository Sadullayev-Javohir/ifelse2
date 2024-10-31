"""To'lov turini tanlash: Foydalanuvchidan to'lov turini (naqd, kartochka) so'rab, har biriga
alohida xabar berish."""

pay = input("To'lov turini naqd yoki karta kiriting: ")

if pay.capitalize() == "karta".capitalize():
    print("Karta tizimiga xush kelibsiz")
elif pay.capitalize() == "naqd".capitalize():
    print("Naqd tizimiga xush kelibsiz")
else:
    print(f"{pay} ? Karta yoki naqd kiriting: ")