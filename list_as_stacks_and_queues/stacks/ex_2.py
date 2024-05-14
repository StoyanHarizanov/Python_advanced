input_text = input()

stack = []

for i in range(len(input_text)):
    if input_text[i] == "(":
        stack.append(i)

    elif input_text[i] == ")":
        print(input_text[stack.pop():i + 1])
