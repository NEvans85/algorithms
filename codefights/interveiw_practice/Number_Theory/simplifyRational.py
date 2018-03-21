"""
A rational number is the ratio of two integers, where the denominator is not zero. We are going to represent the rational number numerator / denominator as the ordered pair (numerator, denominator).

There are many different tuples representing the same rational number. For instance, one-half is (1, 2), (2, 4), (3, 6), etc. Your task is to write a function that, given the numbers numerator and denominator representing the ratio numerator / denominator, returns an array [a, b] of two integers where:

(a, b) represents the same rational number as (numerator, denominator) but in simplified format;
a and b have no non-trivial factors;
b is positive.
Example

For numerator = 3 and denominator = 6, the output should be
simplifyRational(numerator, denominator) = [1, 2].

The number 3 / 6 can be reduced to 1 / 2.

For numerator = 8 and denominator = 5, the output should be
simplifyRational(numerator, denominator) = [8, 5].

There is no way to simplify 8 / 5 any further, as the only factor that 8 and 5 have in common is 1.

For numerator = 8 and denominator = -5, the output should be
simplifyRational(numerator, denominator) = [-8, 5].

One of the requirements is that the denominator should be positive, so 8 / (-5) didn't fit our format, but -8 / 5 does.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer numerator

Guaranteed constraints:
-105 ≤ numerator ≤ 105.

[input] integer denominator

Guaranteed constraints:
-105 ≤ denominator ≤ 105,
denominator ≠ 0.

[output] array.integer

An array that contains two integers a and b, which represent the same ratio as numerator / denominator, but in simplified format.
"""

def simplifyRational(numerator, denominator):

    # Euclidean Algorithm to find the greatest common divisor
    def gcd(num,den):
        a, b = num, den
        while b:
            a,b = b, a % b
        return a

    if numerator == 0:
        return [0,1]
    result = [numerator, denominator]
    if denominator < 0:
        result[1] *= -1
        result[0] *= -1
    divisor = gcd(*result)
    if divisor > 1:
        result = [el / divisor for el in result]
    return result
