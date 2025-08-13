import sys              # For exit
import math
from math import sqrt   # for main
from time import time   # For timeit
import random           # For miller_rabin

import functools        # For profile_memory
import os
import psutil


def timeit(func):
    """Decorator to measure the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def profile_memory(func):
    """Decorator to measure the memory usage of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024 ** 2  # in MB
        result = func(*args, **kwargs)
        mem_after = process.memory_info().rss / 1024 ** 2  # in MB
        print(f"Function {func.__name__} memory usage: {mem_after - mem_before:.4f} MB")
        return result
    return wrapper


@timeit
@profile_memory
def sieve_of_eratosthenes(n)->list:
    """Finds prime in a given range using the Sieve of Eratosthenes. Naive implementation.

    Args:
        n (_type_): Input a positive integer value to look for a range of prime numbers.

    Returns:
        list: A list of primes
    """
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes


@timeit
@profile_memory
def sieve_of_eratosthenes_sqrt(n)->list:
    """Finds prime in a given range using the Sieve of Eratosthenes. New implementation given timing.

    Args:
        n (_type_): Input a positive integer value to look for a range of prime numbers.

    Returns:
        list: A list of primes
    """


    if n <= 1:
        return []

    primes = [True] * (n + 1)  # Initialize all numbers as potentially prime.
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers.

    # Iterate from 2 up to the square root of the n.
    for p in range(2, int(sqrt(n)) + 1):
        if primes[p]:  # If p is prime.
            # Mark all multiples of p as composite (not prime), starting from p*p.
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False

    # Collect the prime numbers.
    result = [i for i in range(n + 1) if primes[i]]
    return result


@timeit
@profile_memory
def trialDivision(limit):
    """Generates a list of prime numbers up to a specified limit using trial division.

    Args:
        limit (_type_): Input a positive integer value to look for a range of prime numbers.

    Returns:
        list: A list of primes
    """
    def is_prime_trial_division(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(2, limit + 1):
        if is_prime_trial_division(num):
            primes.append(num)
    return primes


def _is_composite(n, a, d, s)->bool:
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True


@timeit
def miller_rabin(n, k=5)->bool:  # k is the number of rounds for accuracy.
    """
    Performs the Miller-Rabin primality test.
    Returns True if n is probably prime, False if n is composite.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1  # Equivalent to d = d // 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if _is_composite(n, a, d, s):
            return False
    return True


@timeit
@profile_memory
def sieveOfAtkin(limit):
    """Generates all prime numbers up to a given limit using the Sieve of Atkin.
    https://www.geeksforgeeks.org/dsa/sieve-of-atkin/


    Args:
        limit (int): The upper limit (inclusive) for generating prime numbers.

    Returns:
        list: A list of all prime numbers up to the specified limit.
    """
    # intialise the is_prime array with initial 0 values
    is_prime = [0] * (limit + 1)

    # mark 2 and 3 as prime
    if limit > 2:
        is_prime[2] = 1
    if limit > 3:
        is_prime[3] = 1

    # check for all three conditions
    for x in range(1, int(limit**0.5) + 1):
        for y in range(1, int(limit**0.5) + 1):
            # condition 1
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = (is_prime[n] + 1) % 2
    
            # condition 2
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                is_prime[n] = (is_prime[n] + 1) % 2
                
            # condition 3
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                is_prime[n] = (is_prime[n] + 1) % 2
    
    # Mark all multiples
    # of squares as non-prime
    for i in range(5, limit + 1):
        if i * i > limit:
            break
        if is_prime[i] == 0:
            continue
        for j in range(i * i, limit + 1, i * i):
            is_prime[j] = 0
    
    # store all prime numbers
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i] == 1:
            primes.append(i)
    return primes


@timeit
@profile_memory
def sieveOfAtkinWithBug(limit):
    """Generates all prime numbers up to a given limit using the Sieve of Atkin. 
    Implementation has bug when limit=5

    # https://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python
 

    Args:
        limit (int): The upper limit (inclusive) for generating prime numbers.

    Returns:
        list: A list of all prime numbers up to the specified limit.
    """    


    P = [2,3]
    r = range(1,math.isqrt(limit)+1)
    sieve=[False]*(limit+1)
    for x in r:
        for y in r:
            xx=x*x
            yy=y*y
            xx3 = 3*xx
            xx3yy = xx3 + yy
            n = xx3yy + xx
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = xx3yy
            if n<=limit and n%12==7 : sieve[n] = not sieve[n]
            n = xx3 - yy
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            xx=x*x
            for y in range(xx,limit+1,xx):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P


def main():
    """Main function to execute the Miller-Rabin primality test.
    """
    power = 16
    n = int(pow(2, power) - 1)

    # sieve_of_atkin_primes = sieveOfAtkin(n)
    # print(f"The number of primes in 2^{power}={n} is {len(sieve_of_atkin_primes)}\n")

    # sieve_of_atkin_primes_with_bug = sieveOfAtkinWithBug(n)
    # print(f"The number of primes in 2^{power}={n} is {len(sieve_of_atkin_primes_with_bug)}\n")

    # if sieve_of_atkin_primes == sieve_of_atkin_primes_with_bug:
    #     print("Both methods yield the same primes.")
    # else:
    #     print("The methods yield different primes.")

    trial_division_primes = trialDivision(n)
    print(f"The number of primes in 2^{power}={n} is {len(trial_division_primes)}\n")


if __name__ == "__main__":
    sys.exit(main())