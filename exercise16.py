"""Sovg'a tanlash: Foydalanuvchidan yoshi va jinsi (erkak/ayol) so'ralib, unga mos sovg'a
tavsiya etish."""

age = int(input("Yosh kiriting: "))
jinsi = input("Jinsini kiriting: ")

if jinsi.capitalize() == "ayol".capitalize():
    if (age >= 18):
        print("Ro'mol")
    else:
        print("Qo'g'irchoq")
elif jinsi.capitalize() == "erkak".capitalize():
    if (age >= 18):
        print("Mashina")
    else:
        print("O'yinchoq mashina")