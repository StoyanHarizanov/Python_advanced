numbers = [int(x) for x in input().split()]

reverse_numbers = [print(numbers.pop(), end=" ") for _ in range(len(numbers))]