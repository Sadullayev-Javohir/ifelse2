"""Havoning harorati haqiqiy sonda kiritilsa unga mos holda 30 dan katta bo'lsa
"havo issiq", agar 30 < 20 > 15 "havo iliq" aks holda 15 dan kichik bolsa "havo sovuq"
kabi so'zlarni chiqaring"""

temperature = int(input("Haroratni kiriting: "))

if temperature > 30:
    print(f"{temperature} - Havo issiq")
elif 30 < temperature or temperature >= 15:
    print(f"{temperature} - Havo iliq")
elif 15 > temperature:
    print(f"{temperature} - Havo sovuq")