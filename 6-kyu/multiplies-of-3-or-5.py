"""
Multiplies of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006

"""


def solution(number):
    total = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solution2(number):
    total = 0
    for i in range(0, number):
        if i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total
