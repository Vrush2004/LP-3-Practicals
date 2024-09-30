# Practical 4 :Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.

# Dynamic Programming Approach:
def knapsack_dp(values, weights, capacity):
    n = len(values)
    
    # Create a 2D array to store the maximum value for each subproblem
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item and check if it's more beneficial
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value for the entire capacity will be stored in dp[n][capacity]
    return dp[n][capacity]


# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]  # Values of the items
    weights = [10, 20, 30]  # Corresponding weights of the items
    capacity = 50  # Knapsack capacity

    max_value = knapsack_dp(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value}")