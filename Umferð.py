columns = int(input())
rows = int(input())

count_empty = 0

for _ in range(rows):
    count_empty += str(input()).count('.')

print(count_empty / (columns * rows))