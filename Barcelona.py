length, bag = map(int, input().split())
bags = list(map(int, input().split()))

index = bags.index(bag)

if index >= 2:
    print(f'{index+1} fyrst')
elif index == 1:
    print("naestfyrst")
else:
    print("fyrst")

