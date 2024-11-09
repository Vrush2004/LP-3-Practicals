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

# Branch and Bound Strategy:
import heapq

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound  # Max-heap

# Function to calculate the upper bound
def bound(u, n, capacity, values, weights):
    if u.weight >= capacity:
        return 0

    bound_value = u.value
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        bound_value += values[j]
        j += 1

    if j < n:
        bound_value += (capacity - total_weight) * values[j] / weights[j]

    return bound_value

def knapsack_bb(values, weights, capacity):
    n = len(values)

    # Sort by value-to-weight ratio in decreasing order
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    values = [values[i] for i in items]
    weights = [weights[i] for i in items]

    max_value = 0  # Max value we can carry
    pq = []
    u = Node(-1, 0, 0, 0)  # Starting node
    u.bound = bound(u, n, capacity, values, weights)
    heapq.heappush(pq, u)

    while pq:
        u = heapq.heappop(pq)

        if u.level == n - 1 or u.bound <= max_value:
            continue

        v = Node(u.level + 1, u.value, u.weight, 0)

        # Consider including the current item
        v.weight = u.weight + weights[v.level]
        v.value = u.value + values[v.level]

        if v.weight <= capacity and v.value > max_value:
            max_value = v.value

        v.bound = bound(v, n, capacity, values, weights)

        if v.bound > max_value:
            heapq.heappush(pq, v)

        # Consider excluding the current item
        v = Node(u.level + 1, u.value, u.weight, 0)
        v.bound = bound(v, n, capacity, values, weights)

        if v.bound > max_value:
            heapq.heappush(pq, v)

    return max_value


# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]  # Values of the items
    weights = [10, 20, 30]  # Corresponding weights of the items
    capacity = 50  # Knapsack capacity

    max_value = knapsack_bb(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value}")


# 1. Dynamic Programming Approach
# python
# Copy code
# def knapsack_dp(values, weights, capacity):
#     n = len(values)
# values: List of item values.
# weights: List of item weights.
# capacity: The total capacity of the knapsack.
# n: The number of items.
# python
# Copy code
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
# This initializes a 2D array dp of size (n+1) x (capacity+1) with all values set to 0. The 2D array is used to store the maximum value obtainable for each subproblem of the knapsack (subsets of items and capacity).
# python
# Copy code
#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
#             else:
#                 dp[i][w] = dp[i - 1][w]
# i: Represents the item number (1 to n).
# w: Represents the current capacity being considered (1 to capacity).
# The logic:
# If the weight of the current item is less than or equal to the current capacity (w), we have two choices:
# Include the item: The value becomes values[i-1] + dp[i-1][w-weights[i-1]], which adds the current item and checks the value for the remaining capacity.
# Exclude the item: We simply use the value from the previous row (dp[i-1][w]).
# If the current item can't be added (its weight is greater than w), we exclude it.
# python
# Copy code
#     return dp[n][capacity]
# The value in dp[n][capacity] is the maximum value obtainable with n items and the given knapsack capacity.
# 2. Branch and Bound Approach
# Node Class:

# python
# Copy code
# class Node:
#     def __init__(self, level, value, weight, bound):
#         self.level = level
#         self.value = value
#         self.weight = weight
#         self.bound = bound
# Node: A class to represent a node in the search tree. Each node holds:
# level: The current item being considered (0-based).
# value: The total value accumulated so far.
# weight: The total weight accumulated so far.
# bound: The upper bound of the possible maximum value if the node is expanded further.
# python
# Copy code
# def bound(u, n, capacity, values, weights):
#     if u.weight >= capacity:
#         return 0
#     bound_value = u.value
#     j = u.level + 1
#     total_weight = u.weight
# bound: Function to calculate the upper bound (maximum potential value) that can be obtained from a given node.
# If the weight exceeds the knapsack capacity, the bound is 0 (this node is infeasible).
# Otherwise, we calculate the maximum value by greedily including items until the knapsack is full.
# python
# Copy code
#     while j < n and total_weight + weights[j] <= capacity:
#         total_weight += weights[j]
#         bound_value += values[j]
#         j += 1
# This loop adds items to the knapsack until it can no longer add the full item without exceeding the capacity.
# python
# Copy code
#     if j < n:
#         bound_value += (capacity - total_weight) * values[j] / weights[j]
# If there is still capacity left, it adds a fractional part of the next item to the bound.
# python
# Copy code
#     return bound_value
# Returns the calculated upper bound value.
# python
# Copy code
# def knapsack_bb(values, weights, capacity):
#     n = len(values)
#     items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
#     values = [values[i] for i in items]
#     weights = [weights[i] for i in items]
# Sorting: The items are sorted by their value-to-weight ratio in descending order to prioritize the most valuable items per unit weight.
# python
# Copy code
#     max_value = 0  # Max value we can carry
#     pq = []  # Priority queue to hold nodes
#     u = Node(-1, 0, 0, 0)  # Starting node
#     u.bound = bound(u, n, capacity, values, weights)
#     heapq.heappush(pq, u)
# max_value: Stores the best (maximum) value found.
# pq: A priority queue (heap) to process nodes in order of their bound value.
# u: The initial node with no items included.
# python
# Copy code
#     while pq:
#         u = heapq.heappop(pq)
#         if u.level == n - 1 or u.bound <= max_value:
#             continue
# while pq: The search continues until the queue is empty.
# Check: If the bound of the current node is less than or equal to the best value found so far, skip processing it.
# python
# Copy code
#         v = Node(u.level + 1, u.value, u.weight, 0)
#         v.weight = u.weight + weights[v.level]
#         v.value = u.value + values[v.level]
# v: Create a new node where the next item is included.
# python
# Copy code
#         if v.weight <= capacity and v.value > max_value:
#             max_value = v.value
# Update max_value: If the new node has a valid weight and a higher value, update the maximum value.
# python
# Copy code
#         v.bound = bound(v, n, capacity, values, weights)
#         if v.bound > max_value:
#             heapq.heappush(pq, v)
# Push valid node to pq: If the bound is promising, add the node back to the queue.
# python
# Copy code
#         v = Node(u.level + 1, u.value, u.weight, 0)
#         v.bound = bound(v, n, capacity, values, weights)
#         if v.bound > max_value:
#             heapq.heappush(pq, v)
# Consider excluding the current item and push the corresponding node to the queue if it has a good bound.
# python
# Copy code
#     return max_value
# Finally, return the maximum value that can be achieved.
# Types of Questions the Examiner Might Ask

# Explain the Dynamic Programming Approach for the 0-1 Knapsack Problem.
# Answer: Describe the use of a 2D DP table to store intermediate results and explain the transition between states, where you either include or exclude an item based on its weight and the available capacity.
# How does Branch and Bound improve upon Dynamic Programming in the 0-1 Knapsack Problem?
# Answer: Explain that Branch and Bound uses a greedy approach with upper bound calculations to prune branches of the search tree that are unlikely to lead to optimal solutions, reducing computation time compared to DP in some cases.
# What is the purpose of the bound function in the Branch and Bound approach?
# Answer: The bound function calculates the upper bound of the maximum value that can be obtained from a node, helping to decide whether to explore that node further.
# Can you compare the time and space complexity of the Dynamic Programming and Branch and Bound methods?
# Answer:
# Dynamic Programming: Time complexity is 𝑂(𝑛 × 𝑊) where n is the number of items and W is the knapsack capacity. Space complexity is also O(n×W).
# Branch and Bound: Time complexity is hard to define exactly as it depends on the problem instance and the bounds. Space complexity is O(n) for the node storage in the priority queue.
# How do you decide which method to use for solving the 0-1 Knapsack Problem?
# Answer: Use Dynamic Programming for smaller instances where exact solutions are needed and where time complexity is manageable. Branch and Bound is suitable for larger instances or when heuristic approaches are needed to reduce search space.