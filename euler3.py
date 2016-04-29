# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

# we can save time in a few ways but we probably dont need to
# the simplest approach is the divide by 2 and check

def find_prime(val):
  largest_prime = 2
  while (val>largest_prime):
    if (val%largest_prime==0):
      val = val/largest_prime
      largest_prime = 2
    else:
      largest_prime=largest_prime+1
  return largest_prime

if ( __name__ == '__main__'):
  print(find_prime(600851475143))
