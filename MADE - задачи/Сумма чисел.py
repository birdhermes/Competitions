b = int(input())
a = input().split(maxsplit=b)
result = 0
numbers = list(map(int, a))

result = sum(numbers)

print(result)

