io = open("prob13.txt").read().splitlines()
if io[0] == "X":
    ratio = int(io[2]) / int(io[3])
    print(ratio * int(io[1]))
elif io[1] == "X":
    ratio = int(io[2]) / int(io[3])
    print(int(io[0]) / ratio)
elif io[2] == "X":
    ratio = int(io[0]) / int(io[1])
    print(ratio * int(io[3]))
else:
    ratio = int(io[0]) / int(io[1])
    print(int(io[2]) / ratio)
