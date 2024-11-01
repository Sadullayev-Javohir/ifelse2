"""Juft yoki Toq Son: Foydalanuvchidan son kiritishni so'rang va bu son juft yoki toq 
ekanligini aniqlang."""

num = int(input("Son kiriting: "))

if num % 2 == 0:
    print(f"{num}, Juft son")
elif num == 0:
    print(f"{num}, son nolga teng")
else:
    print(f"{num}, Toq son")