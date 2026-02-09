# n! = n(n-1)(n-2)(n-3)...1

def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

