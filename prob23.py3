from algorthims.dates import days_between
import datetime

io = open("prob23.txt").read().splitlines()

ans = []
for x in io:
    x = x.split("|")
    if x[6] == "true":
        continue
    score = 10000
    if int(x[4]) >= 1000000:
        score += 10000
    elif int(x[4]) < 100:
        score -= 5000
    if int(x[2]) - int(x[3]) == 0:
        score /= 100
    else:
        score /= int(x[2]) - int(x[3])
    if bool(x[5]):
        score += 5000
    # I HAVE NO IDEA WHAT DAY IT WAS ON SO IM ASSUMING TODAY :)
    if days_between(datetime.date.today(), x[7]) <= 7:
        score += 500
    elif days_between(datetime.date.today(), x[7]) > 14:
        score -= 100
    score += int(x[9])
    score += days_between(datetime.date.today(), x[8]) // 7
    ans.append((round(score, 1), f"({round(score, 1)}) {x[0]}, by: {x[1]} [{x[7]}]"))

if ans is None:
    print("You are blocking all (##) posters in your feed, where ## is the number of unique poster names (CaSe "
          "sEnSiTiVe) found in the list")
for x in reversed(sorted(ans)):
    print(x[1])
