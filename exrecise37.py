"""Musbat yoki Manfiy Son: Foydalanuvchi kiritgan son musbat yoki manfiy ekanligini aniqlang.
Agar nol kiritilsa, “Bu nol” deb yozing."""

num = int(input("Son kiriting: "))

if num > 0:
    print(f"{num}, Musbat son")
elif num < 0:
    print(f"{num}, Manfiy son")
else:
    print(f"{num}, Nolga teng")