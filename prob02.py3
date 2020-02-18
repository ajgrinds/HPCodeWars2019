hours, miles, speed = map(lambda x: int(x), open("prob02.txt").read().split(" "))
if speed * hours >= miles:
    print(f'{hours} {miles} {speed}. I will make it!')
else:
    print(f'{hours} {miles} {speed}. I will be late!')
