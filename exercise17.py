"""Reyting tizimi: Agar foydalanuvchining balini 100 dan yuqori bo'lsa, "Reytingni yangilang"
deb chiqarilsin."""

score = int(input("Ball kiriting: "))

if score >= 100:
    print("Reytingni yangilang")
else:
    print('Error')