"""Mashhur kitoblar: Foydalanuvchidan kitob nomini so'rab, agar bu kitob mashhur bo'lsa 
"Buni o'qiganman" deb chiqarish."""

bookName = input("Kitob nomini kiriting: ")
list = ["Qiyomat", "G'arbiy frontda o'zgarish yo'q", "Urush va tinchlik", "Ufq"]

reply = ""
for x in list:
    if bookName.capitalize() == x.capitalize():
        reply = "✅ Buni o'qiganman"
print(reply)