def fibonacci(n: int) -> int:
    fib = [None, 1, 1]
    for i in range(3, n+1):
        f0 = fib[i-2]
        f1 = fib[i-1]
        f2 = f1 + f0
        fib.append(f2)
    return fib[n]

assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025
assert fibonacci(45) == 1134903170