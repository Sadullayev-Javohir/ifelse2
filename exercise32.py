"""Iqlim sharoiti: Foydalanuvchidan haroratni so'rab, agar 0 dan past bo'lsa "Juda sovuq"
deb chiqarish."""

temperature = int(input("Haroratni kiriting: "))

if temperature <= 0:
    print(f"{temperature}, Juda sovuq")
else:
    print(f"{temperature}, issiq")