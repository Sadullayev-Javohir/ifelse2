"""Bajarilgan ishlar: Foydalanuvchidan bajarilgan ishlar sonini so'rab, agar 5 tadan ko'p
bo'lsa "Yaxshi natija" deb chiqarish."""

works = int(input("Nechta ish bajardingiz: "))

if works > 5:
    print("✅ Yaxshi natija")
elif works <= 5:
    print("❌ Yomon natija")