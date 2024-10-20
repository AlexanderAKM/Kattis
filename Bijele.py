chess_set = [1, 1, 2, 2, 2, 8]

received_chess_set = list(map(int, input().split()))

final_set = []

for n in range(len(chess_set)):
    final_set.append(str(chess_set[n] - received_chess_set[n]))

print(' '.join(final_set))