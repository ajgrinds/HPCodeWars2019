io = open("prob14.txt").read().splitlines()
solved = [int(io[0]), int(io[1])]

while len(solved) < int(io[2]):
    solved.append(solved[-1] + solved[-2])

print(",".join(map(lambda x: str(x), solved)))
