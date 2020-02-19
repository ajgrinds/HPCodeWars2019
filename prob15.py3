from algorthims.listCompar import combinations

print(len(combinations(*map(lambda x: int(x), open("prob15.txt").read().split(" ")), 4)))
