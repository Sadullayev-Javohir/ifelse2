"""Sog'liqni tekshirish: Foydalanuvchidan vazn va bo'yini so'rab, BMI ni hisoblang va
sog'liq holatini baholang."""

weight = float(input("Vazn kiriting: "))
height = float(input("Bo'yingiz kiriting: "))

BMI = weight / (height ** 2)

if BMI < 16 or 18.4 >= BMI:
    print(f"{BMI}, Jiddiy kam vazn")
elif BMI <= 18.5 or 24.9 >= BMI:
    print(f"{BMI}, Oddiy")
elif BMI <= 25 or 29.9 >= BMI:
    print(f"{BMI}, Ortiqcha vazn")
elif BMI <= 30 or 34.9 >= BMI:
    print(f"{BMI}, O'rtacha semizlik")
elif BMI <= 35 or 39.9 >= BMI:
    print(f"{BMI}, Og'ir semizlik")
elif BMI >= 40:
    print(f"{BMI}, Juda og'ir semizlik")
