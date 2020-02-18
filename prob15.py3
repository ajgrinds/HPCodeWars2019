from algorthims.listCompar import combinations

b, c = map(lambda x: int(x), open("prob15.txt").read().split(" "))
print(len(combinations(b, c, 4)))
