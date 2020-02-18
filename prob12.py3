io = open("prob12.txt").read().splitlines()
n = int(io[0])
sign = 1
pi = 3

for i in range(2, n*2, 2):
    if sign == 1:
        pi += (4 / (i * (i + 1) * (i + 2)))
    else:
        pi -= (4 / (i * (i + 1) * (i + 2)))
    sign *= -1

print(str(pi).replace(".", "")[int(io[1])])
