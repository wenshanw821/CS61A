""" Homework 1: Control """

# Q1
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda a, b: a-b
    else:
        f = lambda a, b: a+b
    return f(a, b)

# Q2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """

    list = [a, b, c]
    result = 0

    for i in list:
        if i !=min(a,b,c):
            result += i*i
        elif i == min(a,b,c) and i == max(a,b,c):
            return i*i*2
        else:
            continue
    return result


# Q3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors[-2]



# Q4
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result



def with_if_statement(): # This function needs to return 1
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function(): # This function needs to do ANYTHING else.
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    return 1/0 # cause an error, anything else

# Q5
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    def check_even_odd(n):
        if n % 2 == 0:
            return True 
        else:
            return False

    count = 0
    while True:
        print(n)
        if n == 1:
            return count+1
        else:
            if check_even_odd(n):
                n //= 2
            else:
                n = n*3 + 1
        count += 1
    return count


print(hailstone(10))
