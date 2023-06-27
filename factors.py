#/usr/bin/env python3

import sys
import math

def factorize(number):
    factors = []
    sqrt_n = int(math.sqrt(number))
    for i in range(2, sqrt_n + 1):
        while number % i == 0:
            factors.append((i, number // i))
            number //= i
    if number > 1:
        factors.append((number, 1))
    return factors

def factorize_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            for factor in factors:
                print(f'{number}={factor[0]}*{factor[1]}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: factors <file>')
        sys.exit(1)

    filename = sys.argv[1]
    factorize_file(filename)
