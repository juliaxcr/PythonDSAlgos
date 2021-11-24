import math
import string

def factorial(num):
    if num < 0:
        return -1
    if num <= 1:
        return 1
    if num > 1:
        return num * factorial(num-1)

def isPalindrome(x):
    x = str(x)
    if len(x) < 2:
        return True
    if x[0] is not x[len(x) - 1]:
        return False
    return isPalindrome(x[1:len(x) - 1])

########################

# Add any extra import statements you may need here

alphaLower = list(string.ascii_lowercase)
alphaUpper = list(string.ascii_uppercase)
numbers = list(string.digits)

# Add any helper functions you may need here
def rotate(character, rotation_factor):
    if character.isupper():
      idx = alphaUpper.index(character)
      if idx + rotation_factor > len(alphaUpper) - 1:
          idx = (idx + rotation_factor) - len(alphaUpper)
      return alphaUpper[idx + rotation_factor]
    
    if character.islower():
      idx = alphaLower.index(character)
      if idx + rotation_factor > len(alphaLower) - 1:
          idx = (idx + rotation_factor) - len(alphaLower)
      return alphaLower[idx + rotation_factor]
    
    if character.isdigit():
      idx = numbers.index(character)
      if idx + rotation_factor > len(numbers) - 1:
          idx = (idx + rotation_factor) - len(numbers)
      return numbers[idx + rotation_factor]
    
    else:
      return character
      

def rotationalCipher(input, rotation_factor):
  result = ''
  for i in range(len(input)):
    result += rotate(input[i], rotation_factor)
  return result

print(rotationalCipher('Zebra-493?', 3))
print('E' + 6)
print('a' + 6)