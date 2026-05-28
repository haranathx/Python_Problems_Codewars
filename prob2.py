# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).


def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result

print(count_by(2, 5))
print(count_by(3, 4))