import sys

from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm

    setup_code = f"from {algorithm}.{algorithm} import algorithm"

    stmt = f"algorithm({array})"


    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

array = [4, 2, 24, 12, 36, 44]
algos = ["bubble_sort", "inserting_sort"]

print(f"array : {array}")
if len(sys.argv) >= 2:
    if sys.argv[1] in algos:
        run_sorting_algorithm(sys.argv[1], array)
    else: raise ValueError("not a valid algorithm")
else:
        for algo in algos:
           run_sorting_algorithm(algorithm=algo, array=array)
