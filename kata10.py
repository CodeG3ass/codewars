#https://www.codewars.com/kata/5a00e05cc374cb34d100000d

def reverse_seq(n):
    return [i for i in range(n+1) if i!=0][::-1]