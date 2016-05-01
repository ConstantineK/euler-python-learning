'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# so find a number with two factorsish things which sum up to it
# all the numbers must equal 1000 total
# every number must less than 1000 so this seems like brute force time
# though there is probably a much more elegant solution

# I can ignore anything that doesnt have a sqrt
# the numbers themselves have to be fairly small if together they add up to 1000 after being 
import math as m

a = 3
b = (a*a-1)/2
c = b+1


for b in range(1000): # sice they have to add up to 1000 we know that would be the upper bound
  for a in range(1000): 
    c = m.sqrt(a*a + b*b) # set c and test all the things
    if (    
      a<b<c # probably could do some additioal tricks but this is so small idc
      and (a+b+c==1000) 
    ):   
      print(str(a*b*c))