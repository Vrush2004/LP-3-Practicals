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
