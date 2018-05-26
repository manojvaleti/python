n = 14
guess = 100000
while abs(float(guess**2-n)) > 0.00001:
    print guess
    guess = ((n/float(guess))+guess)/2
print guess    
