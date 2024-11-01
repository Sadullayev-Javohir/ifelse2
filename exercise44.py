"""Harfning Turini Aniqlash: Foydalanuvchidan bir harfni so'rang va bu katta yoki kichik
harf ekanligini aniqlang."""

letter = input("1 ta harf kiriting: ")

if letter == letter.upper():
    print(f"{letter}, katta harf")
elif letter == letter.lower():
    print(f"{letter}, kichik harf")