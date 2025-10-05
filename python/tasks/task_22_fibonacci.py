def fibonacci(n):
    """
    Vrátí prvních n členů Fibonacciho posloupnosti.
    """
    f = [0]
    if n == 0:
        return []
    if n > 1:
        f.append(1)
    if n > 1:
        for i in range(2, n):
            f.append(f[i-1]+f[i-2])
    return f
