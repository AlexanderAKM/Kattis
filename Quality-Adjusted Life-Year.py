periods = int(input())
total_quality = 0

for _ in range(periods):
    quality, years = map(float, input().split())
    total_quality += quality * years

print(total_quality)