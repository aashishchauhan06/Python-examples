#!/usr/bin/python

def check_prime(num):
    if(num > 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            print(num)
            
try:
    lower = int(input('Enter start range: '))
    upper = int(input('Enter end range: '))
except:
    exit("Make sure ranges are integers only")

if( lower > 0 or upper > 0 ):
    system.exit("Ranges must be positive numbers")

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper+1):


