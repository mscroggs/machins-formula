from machin import get_decimal, compute_pi, get_ndigits

for n in range(1, 101):
    pi2 = get_decimal(compute_pi(n, n), 1000)
    ndigits = get_ndigits(pi2)
    for m in range(n, -1, -1):
        pi3 = get_decimal(compute_pi(n, m), ndigits + 1)
        if get_ndigits(pi3) < ndigits:
            break
    print(n, m + 1)
