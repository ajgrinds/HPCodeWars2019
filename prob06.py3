def num(n):
    if n == 2:
        return 4
    else:
        return 2 * 2 * (n - 1) + num(n - 1)

print(num(int(open("prob06.txt").read())))
