#https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    new_l = []
    [new_l.append(el) for el in iterable if el not in new_l[len(new_l)-1:]]
    return  new_l

print(unique_in_order('AAAABBBCCDAABBB'))