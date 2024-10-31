"""Ish qidirish: Foydalanuvchidan ish tajribasini so'rab, agar 2 yildan kam bo'lsa 
"Yosh mutaxassis" deb chiqarish."""

experiment = int(input("Ish tajribangizni yilda kiriting: "))

if experiment > 2:
    print("Buyuk mutaxassis")
elif experiment <= 2 and experiment > 0:
    print("Yosh mutaxassis")
elif experiment <= 0:
    print("0 dan katta son kiriting: ")