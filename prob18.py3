num, *io, magicNum = open("prob18.txt").read().splitlines()

magicNum = int(magicNum)
num = int(num)
chosen = []

print("Your MASH Story:")
for m in range(3):
    options = io[(m * num + m) + 1:(m * num) + num + 1 + m]
    i = 0
    while len(options) != 1:
        i = (i + magicNum) % num
        options.pop(i)
    print(f"{io[num * m + m].split(' ')[0]} - {options[0]}")
