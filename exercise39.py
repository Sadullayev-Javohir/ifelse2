"""Yoshni Guruhlash: Foydalanuvchidan yoshini so'rang va u 0-12 yosh bolalar, 13-19 yoshlar
va 20 dan katta kattalar guruhiga kirishini aniqlang."""

age = int(input("Yosh kiriting :"))

if age >= 13:
    print("Kattalar")
elif age >= 0 <= 12:
    print("Yosh bolalar")
