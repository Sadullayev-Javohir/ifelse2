"""Balandlikni Aniqlash: Foydalanuvchidan balandligini so'rang va u qisqa, o'rtacha yoki
baland ekanligini aniqlang."""

height = float(input("Balandlikni kiriting: "))

if height >= 100:
    print("Baland")
elif height >= 50:
    print("O'rtacha")
else:
    print("Qisqa")