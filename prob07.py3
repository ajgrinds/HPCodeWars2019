from algorthims.isPrime import is_prime
import math

for x in open("prob07.txt").read().splitlines():
    x = list(map(lambda _: int(_), x.split(" ")))
    if x[0] == x[1] == 0:
        continue
    if x[1] == 0:
        if x[0] % 2 == 0:
            print(x[0] + 2)
        else:
            print(x[0] + 1)
    if x[1] == 1:
        i = x[0] + 1
        while not is_prime(i):
            i += 1
        print(i)
    if x[1] == 2:
        i = x[0] + 1
        while not math.sqrt(i) == round(math.sqrt(i)):
            i += 1
        print(i)
    if x[1] == 3:
        i = x[0] + 1
        while not abs(i ** (1/3) - round(i ** (1/3))) < 0.00000001:
            i += 1
        print(i)

