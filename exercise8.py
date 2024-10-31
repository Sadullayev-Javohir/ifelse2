"""Yoshni tekshirish: Foydalanuvchining yoshini so'rang va agar 18 dan katta bo'lsa "Kattalar",
aks holda "Bolalar" deb chiqarish."""

age = int(input("Yoshingizni kiriting: "))

if age >= 18:
    print("Kattalar")
else:
    print("Bolalar")
