n = int(input())
a = list(map(int, input().split()))

t = 0
result = 0
delta = n
for i in range(n):
    for j in range(1+i, n):
        if abs( a[i] - a[j]) <= 5:
            current = j-i -1
            if delta > current:
                delta=current
if (delta == n):
    delta = -1
print(delta)
