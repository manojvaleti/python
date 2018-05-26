t = input()
while t :
    count = 0
    n = input()
    str_arr = raw_input().split()
    arr = [int(num) for num in str_arr]
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] ==arr[i-1]:
            count = count +1
    print count
    t = t -1
