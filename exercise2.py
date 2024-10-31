"""
Talaba olgan bahosini tekshiring dastur tuzing agr talaba 5 baho olgan bo'lsa
a'lo, agar 4 baho olgan bo'lsa yaxshi, agar 3 baho olgan bo'lsa qoniqarli
agar 2 baho olgan bo'lsa qoniqarsiz degan so'zlarni ekranga chiqaring
"""

grade = int(input("Talaba olgan bahosini kiriting: "))

if (grade == 5):
    print("A'lo")
elif (grade == 4):
    print("Yaxshi")
elif(grade == 3):
    print("Qoniqarli")
elif(grade == 2):
    print("Qoniqarsiz")
else:
    print("Error")