x_rook, y_rook = map(int, input().split())
x_pawn, y_pawn = map(int, input().split())

if x_rook == x_pawn or y_rook == y_pawn:
    print(1)
else:
    print(2)