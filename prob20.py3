from algorthims.counts import all_indexes
from algorthims.converter import list_to_string
from itertools import permutations

io = open("prob20.txt").read().replace("\n", '').replace("X", "")
io = io[-1] + io[0:-1]

possible = all_indexes(io, "U")
clear = all_indexes(io, "C")
ans = [y for y in [x for x in set(permutations(clear * 4 + possible * 4, 4)) if all([x.count(z) for z in clear])] if y[0] * 10 + y[1] == (y[2] * 10 + y[3]) ** 2]

if len(ans) == 0:
    print("COULD NOT DETERMINE CODE")
elif len(ans) == 1:
    print(f"CODE IS: {list_to_string(ans[0])}")
elif len(ans) < 4:
    for x in ans:
        print(f"POSSIBLE MATH: {list_to_string(x)}")
else:
    print(f"COULD NOT DETERMINE CODE")
