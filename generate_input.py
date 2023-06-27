#/usr/bin/env python3

import random

def generate_input_file(filename, num_numbers):
    with open(filename, 'w') as file:
        for _ in range(num_numbers):
            number = random.randint(6, 1000)  # Generate a random number between 6 and 10000
            file.write(str(number) + '\n')

if __name__ == '__main__':
    filename = 'factors'
    num_numbers = 13

    generate_input_file(filename, num_numbers)
    print(f"Input file '{filename}' generated with {num_numbers} random numbers.")
