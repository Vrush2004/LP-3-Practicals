def fibonacci(n):
    step_count = 0
    if n == 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count
    
    a, b = 0, 1
    step_count += 2  # for initial assignments

    for i in range(2, n + 1):
        step_count += 1  # for each iteration
        a, b = b, a + b
        step_count += 2  # for the assignments inside the loop

    return b, step_count


# Example usage:
n = int(input("Enter the Fibonacci term you want to find: "))
fib_number, steps = fibonacci(n)
print(f"Fibonacci number at position {n} is {fib_number}")
print(f"Total steps taken: {steps}")