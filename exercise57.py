"""Oylik maoshni kiritilsa shunga mos holda daromad solig'i hisoblansin. Agar maosh 10 mln
dan katta bo'lsa 15.5% agar 7 mln katta bo'lsa 12.3% agar 3 mln dan katta bo'lsa 5.6%
hisoblansin. Aks holda 0% qancha miqdorda soliq to'lanishi chiqarilsin."""

maosh = float(input("Maosh kiriting: "))
soliq = ""

if maosh >= 10000000:
    soliq = f"{maosh * 0.155} soliq"
elif maosh <= 7000000:
    soliq = f"{maosh * 0.123} soliq"
elif maosh <= 3000000:
    soliq = f"{maosh * 0.056} soliq"

print(soliq)