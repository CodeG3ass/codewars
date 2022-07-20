#https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    h_l = list(map(int, numbers.split()))
    return ("{0} {1}".format(max(h_l), min(h_l)))