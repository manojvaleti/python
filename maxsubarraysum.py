def subarray(t):
    n = len(t)
    max_global,max_current = t[0],t[0]
    for i in range(n):
        max_current = max(t[i],max_current+t[i])
        max_global = max(max_current ,max_global)
    return max_global;



t = list(map(int,input().split()))
print (subarray(t))


