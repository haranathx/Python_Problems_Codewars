# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    result = 0

    for num in seq:
        result ^= num

    return result


print(find_it([1, 2, 3, 4, 5,3]))