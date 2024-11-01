"""Tezlikni Aniqlash: Foydalanuvchidan avtomobil tezligini so'rang va u tezlikni oshirdimi
yoki normal ekanligini aniqlang."""

fast = float(input("Tezlik kiriting: "))
fastText = ""

if fast >= 100:
    fastText = "Tezlikni oshirdingiz"
else:
    fastText = "Tezlik turg'un"
    
print(fastText)