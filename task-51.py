from math import gcd
from functools import reduce


array1 = [24, 36, 48, 60]
array2 = [12, 18, 24, 36, 72]

def nod(a, b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def mass_gcd(array):
    result = array[0]
    for i in array[1:]:
        result = nod(result, i)
    return result

gcn_array1 = mass_gcd(array1)
gcn_array2 = mass_gcd(array2)

# test
assert(gcn_array1 == reduce(gcd, array1))
assert(gcn_array2 == reduce(gcd, array2))
