advertisements = int(input())

opinions = []

for advertisement in range(advertisements):
    r, e, c = map(int, input().split())
    if e - c > r:
        opinions.append("advertise")
    elif e - c == r:
        opinions.append("does not matter")
    else:
        opinions.append("do not advertise")

for opinion in opinions:
    print(opinion)