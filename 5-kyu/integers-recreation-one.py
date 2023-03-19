"""
Integers: Recreation One
https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

Execution Timed Out, needs optimization
"""


def divisors(number):
    divisors = []
    for num in range(1, number + 1):
        if number % num == 0:
            divisors.append(num)
    squared_divisors = sum([i**2 for i in divisors])
    if (squared_divisors ** (1 / 2)) % 1 == 0:
        return [number, squared_divisors]
    else:
        return None


def list_squared(m, n):
    result = []
    for number in range(m, n + 1):
        result.append(divisors(number))
    return [i for i in result if i is not None]


print(list_squared(1, 250))  # [[1, 1], [42, 2500], [246, 84100]]
