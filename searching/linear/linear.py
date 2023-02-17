
def algorithm(t, v):
    i = 0
    while i < len(t):
        if v == t[i]:
            return True
        i += 1

    return False
