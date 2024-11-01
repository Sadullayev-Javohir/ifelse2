"""Maktabga tayyorgarlik: Foydalanuvchidan maktabga kirishi uchun tayyorgarlik darajasini
so'rab, agar yetarli bo'lmasa "Ko'proq o'qish kerak" deb chiqarish."""

grade = int(input("Tayyorgalik darajasini kiriting: "))

if grade <= 4:
    print(f"{grade}, ko'proq o'qish kerak")
else:
    print(f"{grade}, o'qishingiz shart emas")