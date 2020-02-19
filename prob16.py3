io = open("prob16.txt").read().split(" ")

for x in range(len(io)):
    if x == 0:
        print(io[x], end=" ")
    elif io[x].lower() == io[x - 1].lower():
        if io[x].lower() == "is" or io[x].lower() == "had":
            if io[x].lower() == io[x - 1].lower() == io[x - 2].lower():
                pass
            else:
                print(io[x], end=" ")
        else:
            pass
    else:
        print(io[x], end=" ")
