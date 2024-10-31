"""Kiyinish qoidalari: Foydalanuvchidan ob-havo haqida so'rab, agar yomg'ir yoki qor bo'lsa,
"Ko'ylak kiyma" deb chiqarish."""

weather = input("Ob havo qandayligini kiriting: Misol uchun: Qor")

if weather.capitalize() == "qor".capitalize() or weather.capitalize() == "yomg'ir".capitalize():
    print("Ko'ylak kiyma")
else:
    pass