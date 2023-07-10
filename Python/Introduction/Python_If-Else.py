import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 ==0:          #  only even numbers will have n%2 = 0
        even = True      #  even is a variable of boolean type
    else:
        even = False
    
    if not even:          # checking if the number is odd
        print("Weird")
    elif even and n>2 and n<=5:
        print("Not Weird")
    elif even and n > 6 and n <=20:
        print("Weird")
    else:
        print("Not Weird")
        
