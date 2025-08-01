import time

def quadratic_time(n):
    print(f"\nO(n²) for n={n}")
    start = time.time()

    for i in range(n):
        for j in range(n):
            pass  # No operation inside the inner loop

    end = time.time()

    print(f"Time taken for n = {n} is {end - start:.6f} seconds")

# Example usage
quadratic_time(200)
quadratic_time(400)
quadratic_time(800)
