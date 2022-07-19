#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def func1(m):
    res=1
    for i in list(str(m)):
        res=int(i)*res
    return res


def persistence(n):
    count = 0
    while True:
        if n >= 10:
            count +=1
            n = func1(n)
        else:
            return count