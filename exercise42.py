"""Ikki Sonni Taqqoslash: Foydalanuvchidan ikkita sonni so'rang va ularni qaysi biri katta,
kichik yoki tengligini aniqlang."""

num1 = int(input("1-sonni kiriting: "))
num2 = int(input("2-sonni kiriting: "))

if (num1 > num2):
    print(f"{num1} > {num2}")
elif num1 < num2:
    print(f"{num1} < {num2}")
else:
    print(f"{num1} == {num2}")