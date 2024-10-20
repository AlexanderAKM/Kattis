max_speed = int(input())
num_speeds = int(input())

safe = []

for speed in range(num_speeds):
    place, current_speed = input().split()
    if int(current_speed) < max_speed:
        safe.append(place + " lokud")
    else:
        safe.append(place + " opin")
        
for safe_status in safe:
    print(safe_status)