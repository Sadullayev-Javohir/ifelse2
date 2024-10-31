"""Sertifikat olish: Foydalanuvchi 70% dan yuqori baho olsa, "Sertifikat olishingiz mumkin"
deb chiqarilsin."""

certificate_grade = int(input("100 ballik tizimidagi baho kiriting: "))

if certificate_grade >= 70:
    print(f"{certificate_grade}, Sertifikat olishingiz mumkin.")
else:
    print(f"{certificate_grade}, Sertifikat olishingiz mumkin emas.")