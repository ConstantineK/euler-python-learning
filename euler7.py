'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

# finding primes is an ancient task
# lets try the naieve approach and see how long it takes to get the first 1000 primes
import math as m
from time import sleep, perf_counter as pc
timer = pc()

def primer(nth_prime):  
  primes = [2] 
  x = 3
  while (len(primes) < nth_prime): 
    c = True
    for y in range(3,m.floor(x/2)+1,2): #      
      if x%y==0:
        c = False
    if (c==True):
      primes.append(x)  
    x+=2
  return primes[-1]

print(str(primer(10001)))
print(pc()-timer)
  # 104743
  # 52 seconds, not amazing but this isnt going in production
  # or I would probably drop to numpy/stackoverflow
  