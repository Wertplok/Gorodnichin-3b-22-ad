array1 = [1, 2, 3, 2, 1]

def palindrome_test(array):
    for i in range(len(array)//2):
        if array[i] != array[-i - 1]:
            return False
    return True

assert(palindrome_test(array1) == True)
