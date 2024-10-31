"""Kredit tayyorgarligi: Foydalanuvchining daromadi va qarzini so'rab, agar daromadi 
qarzidan yuqori bo'lsa "Kredit olish mumkin" deb chiqarish."""

inhance = int(input("Daromad kiriting: "))
debt = int(input("Qarz kiriting: "))

if inhance > debt:
    print("✅ Kredit olishingiz mumkin")
else:
    print("❌ Kredit olishingiz mumkin emas")