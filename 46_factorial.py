def factorial(n: int, r: int = 1) -> int:
    return r if n == 1 else factorial(n - 1, r * n)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))
