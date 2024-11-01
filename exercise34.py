"""Savdo so'rovlarini tekshirish: Foydalanuvchidan so'rovlarni so'rab, agar talab yuqori
bo'lsa "Savdo muvaffaqiyatli" deb chiqarish."""

request = int(input("Talab nechta: "))

if request < 5:
    print("Savdo muvaffaqiyatsiz")
else:
    print("Savdo muvaffaqiyatli")
