num_temperatures = int(input())
count = 0

temperatures = list(map(int, input().split()))

for temperature in temperatures:
    if temperature < 0:
        count += 1

print(count)