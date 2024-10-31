"""Parol kuchini tekshirish: Foydalanuvchidan parolni so'rang va agar u 8 ta belgidan kam
bo'lsa, "Parolni kuchaytiring" deb chiqarish."""

password = (input("Parol kiriting: "))

if len(password) < 8:
    print("Parolni kuchaytiring")
else:
    print("Parolingiz kuchli")    