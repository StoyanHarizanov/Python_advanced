stack = []

dict_commands = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None
}

for i in range(int(input())):
    num = input().split()
    var = dict_commands[num[0]](*num[1:])


print(", ".join([str(stack.pop()) for x in range(len(stack))]))

