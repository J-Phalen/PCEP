import math


def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    """
    Returns the factorial of n using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def trampoline(coro):
    """
    Takes a generator-based coroutine, which yields whenever it calls a generator-based coroutine,
    and trampolines using an explicit stack.
    """
    stack = [coro]
    val = None
    while stack:
        top = stack[-1]
        try:
            res = top.send(val)
        except StopIteration as e:  # returned
            val = e.value
            stack.pop()
        else:  # recursed
            stack.append(res)
            val = None
    return val


def afact(n):
    if n < 2:
        return 1
    return n * (yield afact(n - 1))


def fact(n):
    if n < 2:
        return 1
    return n * (fact(n - 1))


trampoline(afact(10000)) == factorial(10000)
trampoline(afact(10000)) == math.factorial(10000)  # No stack overflow!
