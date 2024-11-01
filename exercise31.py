"""Uchuvchi talablari: Foydalanuvchidan uchish uchun yoshi va vaznini so'rab, agar talablarga
mos kelmasa "Uchish mumkin emas" deb chiqarish."""

age = int(input("Yoshingizni kiriting: "))
weight = int(input("Vazningizni kiriting: "))

if (age > 18 and weight > 70):
    print("✈✅ Uchish mumkin")
else:
    print("✈❌ Uchish mumkin emas")