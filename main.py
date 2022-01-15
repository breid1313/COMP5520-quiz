import random
from typing import List

# for repeatability
random.seed(0)

min_x = 1
max_x = 10000
size_x = input("Please enter an integer for the magnitude of X: ")

try:
    size_x = int(size_x)
except ValueError:
    raise RuntimeError("Input must be a base ten integer")


def get_x(start: int, end: int, size: int):
    # generates a list of numbers in the range [start, end] inclusive equal to
    # the size parameter. note that elements in x need not be unique
    nums = []
    for i in range(size):
        nums.append(random.randint(start, end))
    return nums


def is_prime(num: int):
    # returns True if a number is prime and False otherwise
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def get_y_from_x(x: List[int]):
    # generates y by aggregating the prime numbers in x.
    # assumes that x is sorted ascending in order to satisfy the constraint
    # that if i < j then y_i < y_j
    y = []
    for num in x:
        if is_prime(num):
            y.append(num)
    return y


def get_z_from_y(y: List[int]):
    # gets the indexes of y where the index is not a prime number.
    # per the problem, indexes start at 1, not zero
    y_indexes = [i for i in range(1, len(y) + 1)]

    y_not_prime_indexes = []
    for num in y_indexes:
        if not is_prime(num):
            y_not_prime_indexes.append(num)

    z = [y[i - 1] for i in y_not_prime_indexes]

    return z


x = sorted(get_x(min_x, max_x, size_x))
y = get_y_from_x(x)
z = get_z_from_y(y)

with open("y.txt", "w") as f:
    for item in y:
        f.writelines(str(item) + "\n")

with open("z.txt", "w") as f:
    for item in z:
        f.writelines(str(item) + "\n")

print("Done!")
print("x:" + str(x))
print("y:" + str(y))
print("z:" + str(z))
