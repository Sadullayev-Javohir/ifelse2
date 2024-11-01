"""Tatilni Aniqlash: Foydalanuvchidan ta'til vaqtini so'rang va yoz yoki qish ta'tili 
ekanligini aniqlang."""

month = int(input("Ta'til oyini raqamda kiriting: "))

tatilText = ""

if month == 12 or month == 1 or month == 2:
    tatilText = "Qish ta'tili"
elif month == 6 or month == 7 or month == 8:
    tatilText = "Yoz ta'tili"
else:
    tatilText = "Error"

print(tatilText)