"""Qaror qabul qilish: Foydalanuvchiga xohlagan taomni tanlasa,
"Tayyorlashga kirishamiz" deb chiqarish."""

list = ["qozon kabob", "shashlik", "mastava", "norin", "osh", "somsa"]
meat = int(input(f"{str(list)}\ntaom ni raqam orqali tanlang: "))

if meat == 1:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
elif meat == 2:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
elif meat == 3:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
elif meat == 4:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
elif meat == 5:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
elif meat == 6:
    print(f"{list[meat - 1]}, Tayyorlashga kirishamiz")
else:
    print("1 dan 6 gacha istalgan son kiriting: ")