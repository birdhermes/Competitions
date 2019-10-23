
num = list(map(int, input().split()))
nums = list(map(int, input().split()))
mini, maxi = [], []
k, l = [], []

for i in nums:
    if num[1] != 1:
        if i <= num[1] :
            mini.append(i)
        elif i > num[1]:
            maxi.append(i)
    elif num[1] == 1:
        mini.append(0)
        maxi.append(i)


def mean(nums):
    return sum(nums) / max(len(nums), 1)
meanMini = mean(mini)
meanMaxi = mean(maxi)

def ans(meanMini, mini, meanMaxi, maxi):
    for m in mini:
        if len(mini) == 1:
            zz = (m - m) ** 2
            k.append(zz)
        else:
            zz = (meanMini - m) ** 2
            k.append(zz)
    for j in maxi:
        if len(maxi) == 1:
            xx = (j - j)**2
            l.append(xx)
        else:
            xx = (meanMaxi - j)**2
            l.append(xx)
    return sum(l) + sum(k)

print(ans(meanMini, mini, meanMaxi, maxi))