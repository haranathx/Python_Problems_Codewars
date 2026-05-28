# Your task is to make a function that can take any non-negative 
# integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

'''
num = 42145

digits = list(str(num))
digits.sort(reverse=True)

print(digits)
'''

def descending_order(num):
    # Bust a move right here

    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(789456))