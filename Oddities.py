n = int(input())
numbers = [0] * n

for i in range(n):
    numbers[i] = int(input())
    
for number in numbers:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')