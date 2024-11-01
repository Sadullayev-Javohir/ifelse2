"""Dostlar ro'yxati: Foydalanuvchidan dostlar sonini so'rab, agar 5 tadan kam bo'lsa
"Dostlar orttirishingiz mumkin" deb chiqarish."""

mates = int(input("Do'stlar sonini kiriting: "))

if mates < 5:
    print("Do'stlar orttirishingiz mumkin")
else:
    print("Do'stlar orttirishingiz shart emas")