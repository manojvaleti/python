def lcs(a,b,m,n):
    if m == 0 or n == 0:
        return 0;
    else:
        if a[m-1] == b[n-1]:
            return 1+lcs(a,b,m-1,n-1);
        else:
            return max(lcs(a,b,m,n-1) , lcs(a,b,m-1,n));


a = input()
b = input()
m = len(a)
n = len(b)
print (lcs(a,b,m,n))
