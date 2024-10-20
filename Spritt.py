num_classrooms, num_bottles = map(int, input().split())

for classroom in range(num_classrooms):
    num_bottles -= int(input())

if num_bottles >= 0:
    print("Jebb")
else:
    print("Neibb")