guests = int(input())

best_gift = 0
best_name = ''

for _ in range(guests):
    name, gift = input().split()
    gift = int(gift)

    if gift > best_gift:
        best_gift = gift
        best_name = name 

print(best_name)