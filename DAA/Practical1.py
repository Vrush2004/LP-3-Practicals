# Practical 1: Write a program to calculate Fibonacci numbers and find its step count.

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



# Explanation: Defines a function fibonacci that takes an integer n as input. step_count is initialized to zero to keep track of the number of computational steps.
# Examiner Question: Why is step_count initialized to zero?
# Answer: It's initialized to zero so we can increment it with each step taken in the algorithm, allowing us to keep track of the computation steps.
# Explanation: Checks if n is 0 or 1. If n is 0, it returns 0 (the 0th Fibonacci number) and step_count. If n is 1, it returns 1 (the 1st Fibonacci number) and step_count.
# Examiner Question: Why are these conditions checked at the beginning?
# Answer: These conditions cover the base cases of the Fibonacci sequence, where the first two terms are defined as 0 and 1, respectively. This also allows us to avoid unnecessary calculations when n is 0 or 1.
# Explanation: Initializes a and b to the first two numbers in the Fibonacci sequence (0 and 1), and adds 2 to step_count for these assignments.
# Examiner Question: Why are a and b initialized to 0 and 1, and why is step_count incremented by 2?
# Answer: a and b are set to the first two Fibonacci numbers. The step_count is incremented by 2 because initializing a and b is considered as two steps.
# Explanation: This loop runs from 2 to n, updating a and b with each iteration to get the next Fibonacci number. For each loop, step_count is increased by 1 for the iteration and by 2 for updating a and b.
# Examiner Question: Explain how a and b are updated in each iteration and why step_count is incremented.
# Answer: In each iteration, a takes the value of b, and b takes the sum of a and b, giving the next Fibonacci number. step_count is incremented to count the iteration and the two assignments.
# Explanation: After the loop completes, the function returns the nth Fibonacci number (stored in b) and the total step_count.
# Examiner Question: Why does the function return b and step_count?
# Answer: b holds the nth Fibonacci number after the loop completes, and step_count provides the number of computational steps taken to arrive at this result.
# Explanation: Prompts the user to enter the term n for which they want the Fibonacci number. Calls the fibonacci function with n, stores the returned Fibonacci number and steps, and then prints the result.
# Examiner Question: What would happen if n is negative or a non-integer?
# Answer: Since the program currently doesn’t handle negative numbers or non-integers, it may result in unexpected behavior or an error. Additional input validation would be required to handle such cases properly.
# Potential Examiner Questions
# What is the time complexity of this Fibonacci function?
# Answer: The time complexity of this iterative function is 𝑂(𝑛), as it loops n-1 times to compute the nth Fibonacci number.
# What changes would you make if you wanted to calculate large Fibonacci numbers efficiently?
# If n = 5, what will the output be? Explain the step count.
# Answer: For n = 5, the output Fibonacci number is 5. The function will count steps as follows:
# Initial assignment of a and b (+2 steps),
# Four loop iterations with three steps each (one for iteration, two for assignments),
# Total steps: 2 + (4 * 3) = 14 steps.