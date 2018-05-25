#definition for factorial function

def fact(n):
    fact = [1]*(n+1)
    for i in xrange(1,n+1):
	fact[i] = fact[i-1]*i
    return fact[n]

#input

a = input()

#output

print fact(a)
