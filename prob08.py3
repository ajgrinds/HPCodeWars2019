letters = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE']

io = open("prob08.txt").read().split(" ")[:-1]
letter = ""
print(" ".join(io), end=". ")
for x in io:
    if x == 999:
        break
    for z in letters[int(x)]:
        if letters[int(x)].count(z) > letter.count(z):
            letter += z * (letters[int(x)].count(z) - letter.count(z))
print(' '.join(sorted(list(letter))))
