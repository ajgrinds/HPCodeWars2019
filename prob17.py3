io = open("prob17.txt").read().replace(" ", '')

counts = {}

for x in io:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

tenP = []

for x in reversed(sorted(counts)):
    if counts[x] >= 10:
        tenP.append(f"{x}[{counts[x]}]")
    else:
        print(f"{x}[{counts[x]}]", end="")

print(f";{''.join(tenP)}")
