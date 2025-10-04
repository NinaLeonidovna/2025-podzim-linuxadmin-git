# task_22_fibonacci.py

def fibonacci(n: int) -> list[int]:
    """
    Vrátí prvních n členů Fibonacciho posloupnosti.
    """
    f = []
    if n > 0:
        f.append(0)
    if n > 1:
        f.append(1)
    if n > 2:
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
    return f