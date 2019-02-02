
def f1(x: float) -> float:
    return (2 * (x ** 3) + 5) / (3 * (x ** 2))


def f2(x: float, c: float) -> float:
    return c * x * (1 - x)


def x1(k: int, default: float = 1) -> float:
    if k == 0:
        return default
    else:
        return f1(x1(k - 1, default))


def x2(k: int, c: float, default: float = 1) -> float:
    if k == 0:
        return default
    else:
        return f2(x2(k - 1, c, default), c)


with open("q2.txt", "w") as file:
    file.write(f"Sequence value with x_0 = 1 and n from 0 to 20:\n")
    for n in range(0, 21):
        file.write(f"n = {n}: {x1(n)}\n")

    file.write(f"\nSequence value with x_0 from -10 to 10 and n = 20:\n")
    for x_0 in range(-10, 11):
        # 0 leads to div0 error
        if x_0 == 0:
            continue

        file.write(f"x_0 = {x_0}: {x1(20, x_0)}\n")

    file.write(f"\nAlternate sequence computations f(x)=cx(1-x)")
    for c in [0.95, 1.55, 2.0, 3.6, 3.98]:
        file.write(f"\nAlternate sequence value with c = {c}, n from 0 to 20, and x_0 = 0.1\n")
        for n in range(0, 21):
            file.write(f"c = {c}: {x2(n, c, 0.1)}\n")
