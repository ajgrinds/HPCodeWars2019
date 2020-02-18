import datetime

for x in open("prob10.txt").read().splitlines():
    if ":" in x:
        age = int(x.split(":")[1])
        birthdate = x.split(':')[0]
        print(f"Will be {age} on "
              f"{str(int(birthdate.split('-')[0]) + age) + '-' + '-'.join(birthdate.split('-')[1:])} "
              f"if born on {birthdate}", end=" ")
        if age > 99:
            print("(good job!)")
    else:
        a, b = x.split(" ")
        a = map(lambda x: int(x), a.split('-'))
        b = map(lambda x: int(x), b.split("-"))
        print(f"If born on {x.split(' ')[0]}, will be {abs(datetime.datetime(*a) - datetime.datetime(*b)).days // 365} "
              f"years old on {x.split(' ')[1]}")


