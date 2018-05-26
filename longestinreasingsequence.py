def lis(t):
    n = len(t)
    temp = [1]*n
    maximum = temp[0]
    for i in range(1,n):
        for j in range(0,i):
            if t[i] > t[j] and temp[i] < temp[j]+1:
                temp[i] = temp[j]+1
    for i in range(0,n):
        maximum = max(maximum,temp[i])
    return maximum;


t = list(map(int,input().split()))
print (lis(t))
