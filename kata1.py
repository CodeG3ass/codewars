#https://www.codewars.com/kata/56541980fa08ab47a0000040

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

def printer_error(s):
    return  ("{0}/{1}".format( len(''.join([i for i in list(s) if i > 'm'])), len(s)))

print(printer_error(s))