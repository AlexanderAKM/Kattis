javelins = int(input())
total = 0

for _ in range(javelins):
    total += int(input())

print(total - javelins + 1)