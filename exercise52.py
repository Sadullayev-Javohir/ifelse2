"""Kafedagi Buyurtma: Foydalanuvchidan kafeda buyurtma (kofe, choy, sharbat) so'rang va 
buyurtma tayyorlanishini xabar bering."""

kafe = input("Kofe, choy yoki sharbat kiriting: ")

buyurtma = ""

if kafe.lower() == "kofe".lower():
    buyurtma = f"{kafe.lower()}, buyurtmangiz tez orada tayyor bo'ladi"
elif kafe.lower() == "choy".lower():
    buyurtma = f"{kafe.lower()}, buyurtmangiz tez orada tayyor bo'ladi"
elif kafe.lower() == "sharbat".lower():
    buyurtma = f"{kafe.lower()}, buyurtmangiz tez orada tayyor bo'ladi"
else:
    buyurtma = f"{kafe.lower()}, ro'yxatda yo'q"

print(buyurtma)