"""Bahoni Tekshirish: Foydalanuvchidan bahoni so'rang va bahoni A, B, C, D yoki F ga to'g'ri
kelishini aniqlang."""

grade = int(input("Baho kiriting: 1 dan 5 gacha: "))

if grade == 1:
    print(f"{grade} == F")
elif grade == 2:
    print(f"{grade} == D")
elif grade == 3:
    print(f"{grade} == C") 
elif grade == 4:
    print(f"{grade} == B")
elif grade == 5:
    print(f"{grade} == A")
else:
    print("1 dan 5 gacha kiriting: ")
    