"""Kreditni Tasdiqlash: Foydalanuvchidan kredit balini so'rang va u kredit olish uchun mos
kelishini aniqlang."""

kreditBall = float(input("Kredit ballini kiriting: "))

if kreditBall >= 5:
    print("❌ Siz kredit ololmaysiz")
else:
    print("✅ Siz kredit ololasiz")