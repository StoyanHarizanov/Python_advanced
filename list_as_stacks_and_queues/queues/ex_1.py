name = input()

queue = []

while name != "End":
    if name == "Paid":
        while queue:
            a = queue.pop(0)
            print(a)
    else:
        queue.append(name)

    name = input()

print(f"{len(queue)} people remaining.")