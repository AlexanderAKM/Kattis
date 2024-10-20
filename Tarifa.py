monthly_mbs = int(input())
N = int(input())
total = (N+1) * monthly_mbs

for _ in range(N):
    total -= int(input())

print(total)