"""Mashhur kitoblar: Foydalanuvchidan kitob nomini so'rab, agar bu kitob mashhur bo'lsa 
"Buni o'qiganman" deb chiqarish."""

bookName = input("Kitob nomini kiriting: ")
list = ["Qiyomat", "G'arbiy frontda o'zgarish yo'q", "Ufq", "Urush va tinchlik"]
reply = ""

print(bookName)

check = False
for x in list:
    
    if bookName.lower() == x.lower():
        
        check = True
        break
        
if check:
    print("✅ Siz bu kitobni o'qigansiz")
else:
    print("❌ Siz bu kitobni o'qimagansiz")
