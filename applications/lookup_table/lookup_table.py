import math
import random

# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.

    The above goes through every set below, however we're only looking
    for two values within 50,000 Sets
    x position 2, 14
    y position 3, 6

    The goal is to find before it finishes, or finish in under 1min.

    above has a Modulo = to 982451653
    modulo = hash

    math.pow
    math.factorial of the same
    y //= (x, y)
    % = 982451653

    store what's already been compared

    n = search, or number. Location


    """

    # Your code here
    cache = {}
    if (x, y) not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[x, y] = v

    return cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
