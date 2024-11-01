"""Sog'liqni Tekshirish: Foydalanuvchidan belgilari haqida ma'lumot oling va sog'liq holatini
aniqlang (masalan, isitma, yo'tal)."""

analyse = input("Sog'liq belgilarini kiriting: ")

if analyse.lower() == "bosh og'rig'i".lower():
    print(f"{analyse}, Isitma")
elif analyse.lower() == "tomoq og'rig'i".lower():
    print(f"{analyse}, Tomoq ishishi")
elif analyse.lower() == "aksi urish".lower():
    print(f"{analyse}, Grip")
else:
    print("Mavjud belgilarni kiriting: ")