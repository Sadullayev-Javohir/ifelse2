"""Hujjatning amal qilish muddati kiritiladi butun sonda agar hujjat amal qilish muddati
5 kundan o'tib ketgagn bo'lsa "hujjat amal qilish muddati tugadi" aks holda 
"hujjat amal qilish muddati tugagan" kabi so'zlarni chiqaring"""

day = int(input("Kun kiriting: "))

if day >= 5:
    print(f"{day} - Hujjat amal qilish muddati tugadi.")
elif day >= 5 or day >= 0:
    print(f"{day} - Hujjat amal qilish muddati tugamadi")
else:
    print("Error")