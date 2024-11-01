"""Kitob Narxini Tekshirish: Foydalanuvchidan kitob narxini so'rang va narxni arzon, o'rtacha
yoki qimmat ekanligini aniqlang."""

bookPrice = float(input("Kitob narxini kiriting: "))

if bookPrice >= 50:
    print(f"{bookPrice}, narxi qimmat")
elif bookPrice >= 30:
    print(f"{bookPrice}, narxi o'rtacha")
else:
    print(f"{bookPrice}, narxi arzon")