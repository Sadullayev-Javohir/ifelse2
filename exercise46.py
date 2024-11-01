"""Mamlakatni Aniqlash: Foydalanuvchidan mamlakatini so'rang va agar u O'zbekiston bo'lsa,
“Siz O'zbekistondasiz” deb yozing."""

country = input("Mamlakat kiriting: ")

if country.lower() == "O'zbekiston".lower():
    print(f"Siz {country}dasiz")
else:
    print("O'zbekiston deb kiriting: ")