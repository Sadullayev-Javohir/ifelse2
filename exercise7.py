"""Baho baholash: Foydalanuvchidan bahoni so'rang va 90 dan yuqori bo'lsa "A", 80-89 "B",
70-79 "C", 60-69 "D", 60 dan past bo'lsa "F" deb chiqarilsin."""

grade = int(input("Baho kiriting: "))

if grade >= 90:
    print("Sizning darajangiz *A*")
elif grade >= 80:
    print("Sizning darajangiz *B*")
elif grade >= 70:
    print("Sizning darajangiz *C*")
elif grade >= 60:
    print("Sizning darajangiz *D*")
else:
    print("Sizning darajangiz *F*")