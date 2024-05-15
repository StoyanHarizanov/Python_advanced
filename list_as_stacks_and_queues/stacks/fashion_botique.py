
clothes = [int(x) for x in input().split()]

capacity_of_rack = int(input())
current_capacity = capacity_of_rack
racks = 1
while clothes:
    grament = clothes.pop()

    if grament <= current_capacity:
        current_capacity -= grament

    elif grament > current_capacity:
        current_capacity = capacity_of_rack
        racks += 1
        current_capacity -= grament
print(racks)