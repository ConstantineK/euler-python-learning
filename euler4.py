# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# what is a number that mirrors itself that is a product of 2 numbers with three digits
# this will probably be the easiest if I can compare
# strings against reversed strings

x=999   

def ispalindrome(val):
  # find a splitting string and comapre 
  n = str(val)  
  # compare the value as a string fowards and backwards
  if (n == n[::-1]):
    return True
  else:
    return False

#hmp, there is probably a better way than
# brute forcing all the values but its so dang fast.

def three_digit_palinrome():
  numlist = []
  for i in range(999,100,-1):    # 999-100 by 1
    for j in range(i,100,-1): # 999-100 by 1
      if ispalindrome(j*i)==True:        
        numlist.append(int(j*i))
  return sorted(list(numlist))

print(three_digit_palinrome()[-1])
