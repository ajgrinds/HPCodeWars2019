def num(n):
    if n == 1:
        return 1
    else:
        return n * n + num(n - 1)


print(num(int(open("prob05.txt").read())))
