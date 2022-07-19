#https://www.codewars.com/kata/56269eb78ad2e4ced1000013

import math
def find_next_square(sq):
    num = math.sqrt(sq)
    if ((num*10)%10) == 0:
        return  math.pow(num+1, 2)
    else:
        return -1

print(find_next_square(121))