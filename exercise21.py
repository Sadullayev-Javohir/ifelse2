"""Sport turini tanlash: Foydalanuvchidan yoshini so'rab, unga mos sport turini tavsiya
etish."""

age = int(input("Yosh kiriting: "))

if age >= 18:
    print("Og'ir atletika")
elif age < 18:
    print("Yengil atletika")
if age <= 3:
    print("Sizning yoshingiz juda kichik")