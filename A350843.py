# arctan = sum_n=0^inf (-1)^n x^(2n+1) / (2n + 1)
# pi = 16 arctan(1/5) - 4 arctan(1/239)

from fractions import Fraction
with open("pi.txt") as f:
    pi = f.read()


def compute_pi(n, m):
    pi = 0
    for i in range(n):
        pi += 16 * (-1) ** i * Fraction(1, (2 * i + 1) * 5 ** (2 * i + 1))
    for i in range(m):
        pi -= 4 * (-1) ** i * Fraction(1, (2 * i + 1) * 239 ** (2 * i + 1))
    return pi


def get_decimal(n, places=10000):
    N = int(float(n) // 1)
    out = f"{N}."
    n -= N
    for i in range(places):
        n *= 10
        N = int(float(n) // 1)
        out += f"{N}"
        n -= N
    return out


def get_ndigits(approx):
    if not approx.startswith("3."):
        return -1
    for ndigits, (i, j) in enumerate(zip(pi[2:], approx[2:])):
        if i != j:
            break
    return ndigits


for n in range(1, 100):
    pi2 = get_decimal(compute_pi(n, n), 1000)
    ndigits = get_ndigits(pi2)
    for m in range(n, -1, -1):
        pi3 = get_decimal(compute_pi(n, m), 1000)
        if get_ndigits(pi3) < ndigits:
            break
    print(n, m + 1)
