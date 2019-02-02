from numpy import float32 as f


def harmonic(n: int) -> f:
    k: int = 10 ** n
    total: f = f(0)
    one: f = f(1)
    for i in range(1, k + 1):
        total += one / f(i)

    return total


def pow_3(n: int) -> float:
    k: int = 10 ** n
    total: float = 0
    for i in range(1, k + 1):
        total += 1 / (3 ** k)

    return total


with open("q1.txt", "w") as file:
    file.write("Harmonic series partial sums:\n")
    for x in range(1, 9):
        file.write(f"n = {x}: {str(harmonic(x))}\n")

    file.write("\n1/3^k series partial sums:\n")
    for x in range(1, 5):
        file.write(f"n = {x}: {pow_3(x)}\n")
