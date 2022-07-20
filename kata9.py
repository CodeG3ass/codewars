#https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    min_n = min(numbers)
    sum_n = sum(numbers)
    for i in numbers:
        if i+min_n<sum_n and min_n != i:
            sum_n =  i+min_n
    return sum_n
    #return [[i + j for j in numbers if i != j] for i in numbers]

def sum_two_smallest_numbers_2(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))