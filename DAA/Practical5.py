# Practical 5: Write a program to generate binomial coefficients using dynamic programming.

def binomial_coefficient(n, k):
    # Create a 2D table to store the binomial coefficients
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Calculate the binomial coefficients using the recursive relationship
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base case: C(i, 0) = C(i, i) = 1
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Recursive formula: C(i, j) = C(i-1, j-1) + C(i-1, j)
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    
    return C[n][k]


# Example usage
if __name__ == "__main__":
    n = 5  # Number of items
    k = 2  # Number of selections
    result = binomial_coefficient(n, k)
    print(f"Binomial coefficient C({n}, {k}) is {result}")