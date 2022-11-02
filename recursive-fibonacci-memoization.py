'''
In computing, memoization or memoisation is an 
optimization technique used primarily to speed up computer programs 
by storing the results of expensive function calls and returning the cached result 
when the same inputs occur again. 
Memoization has also been used in other contexts (and for purposes other than speed gains), 
such as in simple mutually recursive descent parsing.
Although related to caching, memoization refers to a specific case of this optimization, 
distinguishing it from forms of caching such as buffering or page replacement. 
In the context of some logic programming languages, memoization is also known as tabling.[2]

'''

# library 
# least recently used cache 
from functools import lru_cache

# decorator wich creates a cache for recently calculated results
# when the result is already calculated it only returns the cached value
# otherwise it calculates
@lru_cache(maxsize = 10000)  # by default the maxsize is 128 results
def fibonacci(n):

    # Check that the input is a positive integer
    # raise exception if the parameter isnt a positive int
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n< 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    # print (n, ":", fibonacci(n))   # print fibonacci numbers
    print (fibonacci(n+1) / fibonacci(n))  # print the ratio between the numbers