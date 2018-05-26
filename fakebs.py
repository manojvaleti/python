def binary(a,intial,final,e,i,flag1,flag2):
        count1 = 0
        count2 = 0
        while intial <= final:
            mid = (intial+final)/2
            if a[mid] == e:
                if flag1 > flag2:
                    return (flag1,count2,1)
                else:
                    return (flag2,count1,2)
            if a[mid] > e:
                if i < mid:
                    count1 = count1 + 1
                    final = mid-1
                else:
                    flag1 = flag1+1
                    intial = mid+1
            if a[mid] < e:
                if i > mid:
                    count2 = count2 + 1
                    intial = mid+1
                else:
                    flag2 = flag2 + 1
                    final = mid-1
         
            
t =input()
while t:
    str_arr = raw_input().split()
    a =[int(num) for num in str_arr]
    n = a[0]
    q = a[1]
    str_arr = raw_input().split()
    a = [int(num) for num in str_arr]
    d1 = {}
    for i in range(n):
        d1[a[i]] = i
    b = [int(num) for num in str_arr]
    b.sort()
    d2 = {}
    for i in range(n):
        d2[b[i]] = i
    while q:
        e = input()
        i = d1[e]
        l = d2[e]
        h = n-l-1
        x,p,f = binary(a,0,n-1,e,i,0,0)
        if f == 1:
            if x+p <= l:
                print x
            else:
                print '-1'
        else:
            if x+p<=h:
                print x
            else:
                print '-1'
        q = q-1
    t = t-1 
