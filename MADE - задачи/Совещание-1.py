n = int(input())
a = list(map(int, input().split()))
dct = {}
color = 1
for i in range(n):

    if a[i] not in dct:
        dct[a[i]] = color
        color += 1

result = []
for i in range(n):
    result.append(str(dct[a[i]]))
print(len(dct))
print(' '.join(result))