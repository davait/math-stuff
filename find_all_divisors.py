#! /usr/bin/env python3

import math

def find_all_divisors(given_number):
    # List to store half of the divisors
    divisors = []
    for current_number in range(1, int(math.sqrt(given_number) + 1)):
        if given_number % current_number == 0:
            # Check if divisors are equal
            if given_number / current_number == current_number:
                divisors.append(current_number)
            else: # Otherwise append both
                divisor = int(given_number / current_number)
                divisors.append(current_number)
                divisors.append(divisor)
    return(sorted(divisors))

print(find_all_divisors(100))
