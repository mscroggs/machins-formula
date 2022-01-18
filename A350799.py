from machin import get_decimal, compute_pi, get_ndigits

for n in range(1, 201):
    pi2 = get_decimal(compute_pi(n, n), 1000)
    ndigits = get_ndigits(pi2)
    print(n, ndigits)
