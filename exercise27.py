"""Savdo muvozanati: Foydalanuvchidan xarajat va daromadni so'rab, agar xarajat daromaddan
past bo'lsa "Foyda" deb chiqarish."""

profit = int(input("Daromadni kiriting: "))
expense = int(input("Xarajatni kiriting: "))

if profit > expense:
    print("📈 Foyda")
else:
    print("📉 Bankrot")