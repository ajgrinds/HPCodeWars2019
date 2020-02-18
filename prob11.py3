io = open("prob11.txt").read().splitlines()
sort = [""] * (len(io) - 1)
for x in io[1:]:
    sort[len(sort) - 1 - int(x[0])] = x
print("\n".join(sort))
print("".join([str(x % 10) for x in range(int(io[0].split(" ")[0]))]))
