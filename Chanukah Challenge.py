datasets = int(input())
candles = []

for _ in range(datasets):
    data, days = map(int, input().split())
    candles.append((days ** 2 + days) // 2 + days)

for index, candle in enumerate(candles):
    print(f"{index+1} {candle}")