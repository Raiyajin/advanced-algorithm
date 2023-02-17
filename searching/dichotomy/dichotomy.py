def algorithm(t, v):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            # found v
            return True
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    # got a > b
    return False
