#https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    return ' '.join([i[0].upper()+i[1:].lower() for i in string.split()])

# str.capitalize()
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))