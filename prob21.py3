from algorthims.constants import months, chineseZodiac, zodiacSigns

year, month, day = map(lambda x: int(x), open("prob21.txt").read().split("-"))

sign = 0
if month == 1:
    if day < 20:
        sign = zodiacSigns[0]
    else:
        sign = zodiacSigns[1]
if month == 2:
    if day < 19:
        sign = zodiacSigns[1]
    else:
        sign = zodiacSigns[2]
if month == 3:
    if day < 21:
        sign = zodiacSigns[2]
    else:
        sign = zodiacSigns[3]
if month == 4:
    if day < 20:
        sign = zodiacSigns[3]
    else:
        sign = zodiacSigns[4]
if month == 5:
    if day < 21:
        sign = zodiacSigns[4]
    else:
        sign = zodiacSigns[5]
if month == 6:
    if day < 21:
        sign = zodiacSigns[5]
    else:
        sign = zodiacSigns[6]
if month == 7:
    if day < 23:
        sign = zodiacSigns[6]
    else:
        sign = zodiacSigns[7]
if month == 8:
    if day < 23:
        sign = zodiacSigns[7]
    else:
        sign = zodiacSigns[8]
if month == 9:
    if day < 23:
        sign = zodiacSigns[8]
    else:
        sign = zodiacSigns[9]
if month == 10:
    if day < 23:
        sign = zodiacSigns[9]
    else:
        sign = zodiacSigns[10]
if month == 11:
    if day < 22:
        sign = zodiacSigns[10]
    else:
        sign = zodiacSigns[11]
if month == 12:
    if day < 22:
        sign = zodiacSigns[11]
    else:
        sign = zodiacSigns[0]

print(f"If you were born on {months[month - 1]} {day}, your sign is {sign}.")
print(f"{year} is the year of the {chineseZodiac[year % 12]}.")
