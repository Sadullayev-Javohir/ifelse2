"""Umumiy o'quv natijasi: Foydalanuvchidan 3 ta bahoni olib, ularning o'rtacha qiymatini 
hisoblang va "Yaxshi", "O'rtacha", "Yomon" deb baholang."""

grade1 = float(input("1-bahoni kiriting: "))
grade2 = float(input("2-bahoni kiriting: "))
grade3 = float(input("3-bahoni kiriting: "))

score = (grade1 + grade2 + grade3) / 3

if score >= 4.5:
    print(f"{score}, Yaxshi")
elif score >= 3.5:
    print(f"{score}, O'rtacha")
elif score >= 2.5:
    print(f"{score}, Yomon")