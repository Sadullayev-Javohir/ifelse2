"""Sport Darajasini Aniqlash: Foydalanuvchidan sport darajasini so'rang va u yangi, o'rta
yoki tajribali sportchi ekanligini aniqlang."""

age = float(input("Sport bilan qancha vaqtdan beri shug'ullanasiz? "))

if age >= 3:
    print(f"{age}, tajribali")
elif age >= 2:
    print(f"{age}, o'rta")
elif age >= 0.1:
    print(f"{age}, yangi")
else:
    print("0 dan katta son kiriting: ")