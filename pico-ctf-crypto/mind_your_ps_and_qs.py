#!/usr/bin/env python3
'''
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?
Decrypt my super sick RSA:
c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537
'''
from Crypto.Util import number

# Code geeks for geeks


def phi(n):

    # Initialize result as n
    result = n

    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2
    while(p * p <= n):

        # Check if p is a
        # prime factor.
        if (n % p == 0):

            # If yes, then
            # update n and result
            while (n % p == 0):
                n = int(n / p)
            result -= int(result / p)
            return result
        p += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if (n > 1):
        result -= int(result / n)
    return result


C = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
E = 65537
N = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543

# To calculete
#TOTIENT_N = 1584586296183412107468474423529992275939442909666671958851095205636494743947753520


TOTIENT_N = phi(N)
D = pow(E, -1, TOTIENT_N)
RESULT = pow(C, D, N)
print(number.long_to_bytes(RESULT).decode("utf-8"))
