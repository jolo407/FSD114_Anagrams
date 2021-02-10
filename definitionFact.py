def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def fib(n):
    if n < 2: # base case
        return n
    return fib(n-1) + fib(n-2)