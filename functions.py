"""
Auxiliary methods for number theoretic algorithms in this set.
These do not use streamlit.
"""
import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y


def multiplicative_inverse(a, n):
    d, x0, y0 = extended_gcd(a, n)

    if d != 1:
        return 0
    else:
        return x0


def sieve(n):
    if n<2:
        return []

    the_list = list(range(2, n+1))      # the list of all numbers from 2 to n
    first_unmarked = 0                  # the index of the first unmarked entry

    while the_list[first_unmarked] <= int(math.floor(math.sqrt(n))):
        # mark all multiples of the first unmarked entry
        for i in range(first_unmarked+1, len(the_list)):
            if the_list[i] % the_list[first_unmarked] == 0:
                the_list[i] = 0

        # find the next unmarked entry
        j = first_unmarked+1
        while the_list[j] == 0:     # this entry is already marked
            j = j+1
        first_unmarked = j

    return [p for p in the_list if p > 0]


def phi(n):
    n_aux = n
    phi_aux = 1

    small_primes = sieve(int(math.sqrt(n_aux))+1)
    for p in small_primes:
        if n_aux % p == 0:               # we came across another prime factor of n
            n_aux = n_aux // p             # first settle the case if largest exponent of p in n is 1
            phi_aux = phi_aux * (p-1)

            while n_aux % p == 0:        # and then settle the case if the exponent is larger than 1
                n_aux = n_aux // p
                phi_aux = phi_aux * p

        if p > n_aux:                    # perhaps we have already exhausted possible prime factors
            break

    if n_aux > math.sqrt(n):             # n also has a single prime factor larger than sqrt(n)!
        phi_aux = phi_aux * (n_aux-1)

    return phi_aux
