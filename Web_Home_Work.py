list_fibonacci = []


def fibonacci(a=0, b=1, n=1):
    if len(list_fibonacci) == 0:
        list_fibonacci.append(0)
        fibonacci(a, b, n)
    elif len(list_fibonacci) < n:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            list_fibonacci.append(c)
        fibonacci(a, b, n)
    elif len(list_fibonacci) == n:
        return list_fibonacci


fibonacci(n=8)

print(list_fibonacci)
