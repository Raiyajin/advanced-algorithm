import sys

from timeit import repeat


def run_searching_algorithm(algorithm, array, value):
    # Set up the context and prepare the call to the specified
    # algorithm

    setup_code = f"from {algorithm}.{algorithm} import algorithm"

    stmt = f"algorithm({array}, {value})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


custom_array = [4, 8, 24, 25, 36, 44]
algos = ["dichotomy", "linear"]

print(f"array : {custom_array}")

v = input("Input the value to search in the array : ")

if len(sys.argv) >= 2:

    if sys.argv[1] in algos:
        run_searching_algorithm(algorithm=sys.argv[1], array=custom_array, value=v)

    else:
        raise ValueError("not a valid algorithm")

else:
    for algo in algos:
        run_searching_algorithm(algorithm=algo, array=custom_array, value=v)
