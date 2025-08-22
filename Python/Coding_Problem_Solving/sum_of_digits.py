import timeit
import sys

# Allow Python to handle larger integers safely (for big test cases)
sys.set_int_max_str_digits(20000)

# ------------------------------
# Different Approaches
# ------------------------------

# Approach 1: String Conversion + Generator
def sum_digits_str(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

# Approach 2: Arithmetic Loop
def sum_digits_math(n: int) -> int:
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Approach 3: Recursion
def sum_digits_recursive(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_digits_recursive(n // 10)

# Approach 4: Built-in map + sum
def sum_digits_builtin(n: int) -> int:
    return sum(map(int, str(abs(n))))


# ------------------------------
# Benchmarking
# ------------------------------
def benchmark():
    # Small input
    small_number = 123456789
    # Large input (10,000 digits, all 9's)
    large_number = int("9" * 10000)

    print(f"small_number is {small_number}")
    print(f"large_number is {large_number}")

    funcs = {
        "String Conversion": lambda: sum_digits_str(large_number),
        "Arithmetic Loop": lambda: sum_digits_math(large_number),
        "Built-in map+sum": lambda: sum_digits_builtin(large_number),
    }

    # Print results
    print("🔹 Benchmark: Sum of Digits Methods\n")

    for name, func in funcs.items():
        t = timeit.timeit(func, number=10)
        print(f"{name:<20} -> {t:.6f} seconds (10 runs, 10,000-digit number)")

    # Recursion benchmark (only on smaller input due to recursion depth limits)
    t = timeit.timeit(lambda: sum_digits_recursive(int("9" * 1000)), number=10)
    print(f"{'Recursion (1000 digits)':<20} -> {t:.6f} seconds (10 runs, 1000-digit number)")


# ------------------------------
# Main Driver
# ------------------------------
if __name__ == "__main__":
    # Quick test
    num = 124
    print(f"Input: {num}")
    print("Approach 1 (String):", sum_digits_str(num))
    print("Approach 2 (Math):", sum_digits_math(num))
    print("Approach 3 (Recursion):", sum_digits_recursive(num))
    print("Approach 4 (Builtin):", sum_digits_builtin(num))
    print("\n")

    # Run benchmark
    benchmark()
