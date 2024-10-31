"""Ishni baholash: Foydalanuvchidan ish natijasini so'rab, "Qoniqarli", "Yaxshi", 
"Mukammal" deb baholash."""

result = int(input("Ish natijasini 3 dan 5 gacha kiriting: "))

if result >= 5:
    print("Mukammal")
elif result >= 4:
    print("Yaxshi")
elif result >= 3:
    print("Qoniqarli")
else:
    print("3 dan 5 gacha oraliqdagi son kiriting: ")