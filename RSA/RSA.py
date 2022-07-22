# SIMPLE RSA IMPLEMENTATION 
# @sutterseba
# Educational purpose only

from math import sqrt
from random import randint

# Maximum size of prime numbers p, q
# This implementation does not support real world key size
MAX = 2048

def gcd (a, b):
    """Returns the greates common divisor of a and b"""

    while b:
        a, b = b, a % b
    return a


def is_prime (n):
    """Returns true if n is prime"""

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def search_prime (max):
    """Searches for and returns prime number within given limit"""

    p = randint(3, max)

    # Making sure p is odd
    if p & 1 == 0:
        p += 1

    while not is_prime(p):
        p += 2

    # Error if no prime in range
    if p > max:
        raise ValueError("No prime number in given limits")

    return p


def init_mode ():
    """Generates mode n and totient of n"""

    p = search_prime(MAX)
    q = search_prime(MAX)

    # Catching the unlikely event of identical prime numbers
    if p == q:
        raise ValueError("Prime numbers identical")

    n = p * q
    phi = (p - 1) * (q - 1)

    return n, phi


def get_keypair (phi):
    """Returns the key parameters d and e"""

    e = randint(1, phi - 1)

    while gcd(e, phi) != 1:
        e = randint(1, phi - 1)

    d = pow(e, -1, phi)

    return e, d


def encrypt (m, e, n):

    # This implementation does not work with large messages
    if m > n:
        raise ValueError("Message larger than mode")

    return (m ** e) % n


def decrypt (c, d, n):

    # This implementation does not work with large ciphers
    if c > n:
        raise ValueError("Cipher larger than mode")
    
    return (c ** d) % n
