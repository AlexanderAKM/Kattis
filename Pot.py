addends = int(input())
total = 0
for n in range(addends):
    wrong_number = int(input())
    power = wrong_number % 10
    number = wrong_number // 10
    total += number ** power

print(total)