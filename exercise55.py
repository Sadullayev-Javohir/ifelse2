"""Maktab Bahosi: Foydalanuvchidan maktab bahosini so'rang va u yuqori, o'rtacha yoki past
baho ekanligini aniqlang."""

grade = float(input("Maktab bahosini kiriting :"))
gradeText = ''

if grade >= 5:
    gradeText = f"{grade}, Yuqori"
elif grade >= 4:
    gradeText = f"{grade}, O'rtacha"
elif grade >= 2:
    gradeText = f"{grade}, Past"
else:
    gradeText = "2 dan 5 gacha kiriting: "

print(gradeText)