
def algorithm(t, v):
    i = 0
    while i < len(t):
        if v == t[i]:
            return True
        i += 1

    return False

if __name__ == "__main__":

    array = [4, 8, 24, 25, 36, 44]

    print(array)

    val = int(input("Input the value to search in the array : "))

    print(algorithm(array, val))