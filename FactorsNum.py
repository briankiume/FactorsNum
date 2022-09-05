def factorsNum(n):
    factors = []
    for x in range(1, n + 1):
        if n % x == 0:
            factors.append(x)

    return len(factors)


print(factorsNum(24))
