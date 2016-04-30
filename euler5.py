# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?
# eg lowest common multiple
# instead of checking, why not just construct it?

import fractions

def range_finder():  
  result = 1
  for i in range(1,21):  
    result =  result* (i // fractions.gcd(i,result))    
  # effectively check if the value we currently have
  # is divisible by the next value in the list cleanly
  # if it isnt, multiply to get the next value that would be
  # cleanly divisble     
  return result

smallest = range_finder()
print(smallest)