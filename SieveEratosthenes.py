import math


def sieve(n):
    """
    Given a positive integer n,
    use the sieve of Eratosthenes to find all primes not exceeding it.

    :param n: the integer up to which we look for primes
    :return:  the list of primes up to n
    """
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

    return [p for p in the_list if p>0]


if __name__=="__main__":
    print(f'Primes up to 100 are: {sieve(100)}')
    print(f'Primes up to 10,000 are: {sieve(10000)}')
