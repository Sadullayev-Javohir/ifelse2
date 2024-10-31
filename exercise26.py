"""Futbol jamoasini tanlash: Foydalanuvchidan sevimli futbol jamoasini so'rab, agar jamoa 
yutgan bo'lsa "Tabriklaymiz!" deb chiqarish."""

fanTeam = input("Sevimli futbol jamoangiz: ")

if fanTeam.capitalize() == "real madrid".capitalize():
    print("😥 Yutqazdingiz")
elif fanTeam.capitalize() == "barcelona".capitalize():
    print("😉 Tabriklaymiz")
else:
    print("Real madrid yoki barcelona kiriting: ")