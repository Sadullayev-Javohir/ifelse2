"""Yozgi ta'til rejalari: Foydalanuvchidan yozgi ta'til rejalarini so'rab, agar rejasi
bo'lsa "Yozda sayohatga chiqamiz" deb chiqarish."""

reja = input("Yozgi ta'til rejangiz bormi? Ha yoki Yo'q: ")

if reja.capitalize() == "ha".capitalize():
    print("✅ Yozda sayohatga chiqamiz")
elif reja.capitalize() == "yo'q".capitalize():
    print("❌ Yozda sayohatga chiqmaymiz")
else:
    print("Ha yoki yo'q deb javob bering!")