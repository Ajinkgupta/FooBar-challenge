def solution(x, y):
    m = int(x)
    f = int(y)
    gens = 0
    while True:
        if m == 1 and f == 1:
            return str(gens)
        elif m < 1 or f < 1 or m == f:
            return "impossible"
        else:
            if m > f:
                if m > 10 * f:
                    multi = (int(m / f) - 1)
                    gens += multi
                    m = m - (multi * f)
                else:
                    m -= f
                    gens += 1
            else:
                if f > 10 * m:
                    multi = (int(f / m) - 1)
                    gens += multi
                    f = f - (multi * m)
                else:
                    f -= m
                    gens += 1
