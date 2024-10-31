"""Bojxona qoidalari: Foydalanuvchidan xorijdan olib kelgan mahsulotni so'rab, agar qiymati
100$ dan yuqori bo'lsa, "Boj to'lashingiz kerak" deb chiqarish."""

product = float(input("Mahsulot narxini kiriting: "))

if product > 100:
    print("Boj to'lashingiz kerak")
else:
    print("Boj to'lashingiz shart emas")