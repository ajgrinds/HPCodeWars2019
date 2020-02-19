password, *io = open("prob19.txt").read().splitlines()

key = 0
add = 1
for x in password:
    key += add * ord(x)
    add *= -1
print(f"Key = {key}")
for x in io:
    for z in x:
        print(hex(ord(z) * key)[2:], end=',')
    print()

