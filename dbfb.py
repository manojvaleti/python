def fib(n,x,y):
    a,b = x,y
    for i in range(n):
        a,b = b%(10**9+7),(a+b)%(10**9+7)
    return a
     
t = input()
while t:
    diff1 = 0
    diff2 = 0
    str_arr = raw_input().split()
    a = [int(num) for num in str_arr]
    m = a[0]
    n = a[1]
    str_arr = raw_input().split()
    a = [int(num) for num in str_arr]
    str_arr = raw_input().split()
    b = [int(num) for num in str_arr]
    result = 0
    for i in b:
        diff1  = diff1 + (i-b[0])
    for i in a:
        diff2 = diff2 + (i - a[0])
    p = fib(n-1,a[0],b[0])%(10**9+7)
    sum1 = ((m*p)%(10**9+7)+ (fib(n-1,0,1)*diff1) %(10**9+7))%(10**9+7)
    result = ((m*sum1)%(10**9+7)+ (m*fib(n-1,1,0)*diff2) % (10**9+7))%(10**9+7)
    print result
    t = t-1  
