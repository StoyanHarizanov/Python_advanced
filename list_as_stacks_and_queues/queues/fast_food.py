from collections import deque

quantity_of_food = int(input())
orders = deque()
numbers = [orders.append(int(x)) for x in input().split()]
print(max(orders))

while orders:
    order = orders.popleft()
    if quantity_of_food < order:
        orders.appendleft(order)
        break

    elif int(order) <= quantity_of_food:
        quantity_of_food -= order

if orders:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
elif not orders:
    print("Orders complete")