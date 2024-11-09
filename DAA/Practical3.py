# Practical 3 : Write a program to solve a fractional Knapsack problem using a greedy method.

# Function to calculate the maximum value of items that can be put in the knapsack
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to get the maximum value in the knapsack
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in decreasing order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0  # Total value in knapsack
    for item in items:
        if capacity - item.weight >= 0:
            # If the whole item can be added, add its full value
            capacity -= item.weight
            total_value += item.value
        else:
            # If only part of the item can be added, add proportional value
            total_value += item.value * (capacity / item.weight)
            break  # Knapsack is full

    return total_value


# Example usage
if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]  # Example items
    capacity = 50  # Knapsack capacity

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value:.2f}")


# Explanation:
# This is a class representing an item. It has two properties: value (the value of the item) and weight (the weight of the item). These are passed as arguments to the constructor __init__ when creating an instance of the Item class.
# The Item class is used to create objects that hold information about items that can be placed in the knapsack.
# Explanation:
# Sorting Items:
# This line sorts the items by their value-to-weight ratio in decreasing order. The value-to-weight ratio for an item is calculated as value / weight.
# Sorting in decreasing order ensures that the algorithm picks the items with the highest value per unit weight first, which is the greedy approach in the fractional knapsack problem.
# lambda x: x.value / x.weight is an anonymous function that takes an item x and calculates its value-to-weight ratio.
# reverse=True ensures the sorting is done in descending order (highest ratio first).
# This variable total_value will accumulate the total value of the items that are selected for the knapsack. It is initialized to 0 at the beginning.
# Greedy Selection:
# This for loop iterates over the sorted list of items.
# For each item, it checks if the current item can fit entirely into the remaining capacity of the knapsack (capacity - item.weight >= 0).
# If yes, the item is fully added to the knapsack.
# The capacity of the knapsack is reduced by the weight of the current item, and the value of the item is added to the total value of the knapsack.
# Handling Fractional Items:
# If the item cannot fully fit in the knapsack (i.e., if capacity - item.weight < 0), the program adds a fraction of the item to the knapsack.
# The fraction of the item added is proportional to the remaining capacity, which is calculated as capacity / item.weight. The value added to the knapsack is also proportional to the fraction of the item, calculated as item.value * (capacity / item.weight).
# After this, the loop breaks because the knapsack is now full and no further items can be added.
# Returning the Total Value:
# After all items are either fully or partially added to the knapsack, the function returns the total value (total_value) accumulated in the knapsack.
# Example Input:
# Here, we create three items using the Item class, each with a value and a weight:
# Item(60, 10) means an item with a value of 60 and a weight of 10.
# Item(100, 20) means an item with a value of 100 and a weight of 20.
# Item(120, 30) means an item with a value of 120 and a weight of 30.
# The knapsack capacity is set to 50 units.
# Calling the Function:
# The function fractional_knapsack is called with the knapsack's capacity and the list of items, and it returns the maximum value the knapsack can hold.
# Printing the Result:
# The result is printed with the maximum value in the knapsack formatted to two decimal places ({max_value:.2f}).
# Maximum value in the knapsack: 240.00
# Explanation of the Output:
# Items Sorted by Value-to-Weight Ratio:

# For the three items, the value-to-weight ratios are:
# Item 1: 60 / 10 = 6.0
# Item 2: 100 / 20 = 5.0
# Item 3: 120 / 30 = 4.0
# After sorting by value-to-weight ratio in decreasing order, the order of items becomes: Item 1 (6.0), Item 2 (5.0), Item 3 (4.0).
# Greedy Selection:
# First, Item 1 (60 value, 10 weight) is added completely to the knapsack, reducing the capacity to 40 (50 - 10 = 40).
# Next, Item 2 (100 value, 20 weight) is added completely, reducing the capacity to 20 (40 - 20 = 20).
# Finally, Item 3 (120 value, 30 weight) is partially added, as only 20 units of capacity are left. The proportion of Item 3 added is (20 / 30) of its total value, which is 120 * (20 / 30) = 80. This is added to the total value, and the knapsack is full.
# So, the total value in the knapsack is: 60 (Item 1) + 100 (Item 2) + 80 (part of Item 3) = 240.

# Examining Possible Questions:
# Explain the Greedy Approach:
# "Why do we use a greedy approach for the knapsack problem? Explain with an example."
# The greedy approach works by selecting items based on the maximum value-to-weight ratio, ensuring the maximum value is achieved by taking the most valuable items first. If necessary, the algorithm takes fractions of items.
# What is the time complexity of this algorithm?
# The sorting step (items.sort()) takes O(n log n), where n is the number of items. The loop iterating over the items takes O(n). Therefore, the overall time complexity is O(n log n).
# What is the difference between the 0/1 Knapsack and Fractional Knapsack?
# In 0/1 Knapsack, we either take the whole item or leave it, whereas in Fractional Knapsack, we can take fractions of the items based on available space. The fractional knapsack problem is solvable using the greedy approach, while 0/1 knapsack requires dynamic programming.