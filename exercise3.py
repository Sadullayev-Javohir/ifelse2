"""Oy raqamini ekrandan kiritilsa shunga mos faslni ekranga cjiqaring.
Masalan: 12, 1 yoki 2 raqam kiritilsa Qish fasili deb chiqaring"""

month = int(input("Oy kiriting: "))

if (month == 1 or  month == 2 or month == 12):
    print("Qish")
elif (month == 3 or month == 4 or month == 5):
    print("Bahor")
elif (month == 6 or month == 7 or month == 8):
    print("Yoz")
elif (month == 9 or month == 10 or month == 1):
    print("Kuz")
else:
    print("Error")