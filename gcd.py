#!/usr/bin/python

#definition for gcd fuction:

def gcd(a,b):
    if b == 0:
       return a
    else:
       return gcd(b, a%b)

#here input is taken in two different lines
a = input()
b = input()

#output
print gcd(a,b)


#to take input on the space line we can use a,b = map(int,raw_input().split())
