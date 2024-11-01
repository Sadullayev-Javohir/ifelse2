"""Havo Haroratini Aniqlash: Foydalanuvchidan havo haroratini so'rang va u juda issiq, iliq,
sovuq yoki juda sovuq ekanligini aniqlang."""

temperature = int(input("Havo haroratini kiriting: "))

if (temperature > 40):
    print(f"{temperature}, Juda issiq")
elif temperature > 20:
    print(f"{temperature}, Issiq")
elif temperature > 10:
    print(f"{temperature}, Iliq")
elif temperature > 0:
    print(f"{temperature}, Sovuq")
elif temperature <= 0:
    print(f"{temperature}, Juda sovuq")