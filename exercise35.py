"""Dars tayyorgarligi: Foydalanuvchidan dars tayyorgarligi darajasini so'rab, agar yetarli
bo'lmasa "Boshqa darslar oling" deb chiqarish."""

grade = int(input("Dars tayyorgarlikgi darajasini kiriting, maximum 100: "))

if grade <= 70:
    print("Boshqa darslar oling")
else:
    print("Boshqa darslar olish shart emas")