#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """
    Function that determine the winner of the game
    args:
        -x: number of rounds to be played
        -nums: array of the sequence of the prime number
    Return:
        - winner if exists otherwise None
    """
    prayer = {"Maria": 0, "Ben": 0}
    for i in range(1, x):
        arr_prime = generate_prime_array
        if (len(arr_prime) == 0):
            prayer["Ben"] += 1
        else:
            for count in range(1, len(arr_prime)):
                if (count % 2 == 0):
                    prayer["Ben"] += 1
                else:
                    prayer["Maria"] += 1

    if (prayer["Maria"] > prayer["Ben"]):
        return "Maria"
    elif (prayer["Ben"] > prayer["Maria"]):
        return "Ben"
    else:
        return None


def generate_prime_array(n):
    """the function that generates the sequence n of prime numbers
    args:
        - n: sequence times
    Return:
        - the array of prime number
    """

    prime_arr = []
    for i in range(1, n):
        if (is_prime(i)):
            prime_arr.append(i)

    return prime_arr


def is_prime(number):
    """check if a number is prime
    arg:
    -number: a number to be checked
    Return:
        -True: if is a prime
        -False: if is not a prime
    """
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True