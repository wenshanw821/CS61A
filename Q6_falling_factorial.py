def falling(n,k):
    '''compute the falling factorial of n to depth k. '''

    result = 1

    for i in range(n, n-k, -1):
        result *= i
    return result

result = falling(6,3)
print(result)