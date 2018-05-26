def binary(n,k):
    c = [0 for x in xrange(k+1)]
    c[0] = 1
    for i in range(1,n+1):
        j  = min(i,k)
	while j:
	    c[j] = c[j-1]+c[j-2]
	    j = j-1
    return c[k]

n = input()
k = input()
print binary(n,k)
