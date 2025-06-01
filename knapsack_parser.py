import os
from pathlib import Path


class KnapsackInstance:
    def __init__(self, n_items, capacity, values, weights, optimal_solution=None):
        self.n_items = n_items
        self.capacity = capacity
        self.values = values
        self.weights = weights
        self.optimal_solution = optimal_solution

    def print(self):
        print(f"Number of items: {self.n_items}")
        print(f"Capacity: {self.capacity}")
        print(f"First few values: {self.values[:5]}...")
        print(f"First few weights: {self.weights[:5]}...")

        # Calculate total value and weight
        total_value = sum(self.values)
        total_weight = sum(self.weights)
        print(f"Total value of all items: {total_value}")
        print(f"Total weight of all items: {total_weight}")

        if self.optimal_solution is not None:
            sum_capacity = sum(
                weight
                for weight, is_selected in zip(self.weights, self.optimal_solution)
                if is_selected
            )
            sum_value = sum(
                value
                for value, is_selected in zip(self.values, self.optimal_solution)
                if is_selected
            )
            print(
                f"Optimal solution capacity: {sum_capacity}, total value: {sum_value}"
            )

    @classmethod
    def parse_knapsack_file(cls, file_path):
        """
        Parse a knapsack problem instance or solution file.

        Instance file format:
        - First line: number_of_items capacity
        - Subsequent lines: value weight (one pair per line)

        Args:
            file_path (str): Path to the knapsack instance file
            is_solution_file (bool): Whether this is a solution file

        Returns:
            KnapsackInstance: Object containing the problem instance data
        """
        values = []
        weights = []

        with open(file_path, "r") as f:
            lines = [
                line.strip() for line in f if line.strip() and not line.startswith("//")
            ]

            # Parse first line for number of items and capacity
            n_items, capacity = map(int, lines[0].split())
            assert n_items > 0, "Number of items must be greater than zero."
            assert capacity > 0, "Capacity must be greater than zero."
            assert len(lines) >= n_items + 1, (
                "File does not contain enough lines for the specified number of items."
            )

            # Parse values and weights
            for i in range(1, n_items + 1):
                if i < len(lines):
                    value, weight = map(int, lines[i].split())
                    assert value > 0, "Value must be non-negative."
                    assert weight > 0, "Weight must be non-negative."
                    values.append(value)
                    weights.append(weight)

            if len(lines) > n_items + 1:
                # If there are more lines, assume they contain an optimal solution
                optimal_solution = list(map(int, lines[n_items + 1].split()))
            else:
                optimal_solution = None

        return cls(n_items, capacity, values, weights, optimal_solution)


def main():
    # Test with instances of different sizes
    instances = [
        r"c:\Users\wtan\phd-optimacs\AA-all-repos\instances\knapsack-01\low-dimensional\f3_l-d_kp_4_20",
        r"c:\Users\wtan\phd-optimacs\AA-all-repos\instances\knapsack-01\low-dimensional\f1_l-d_kp_10_269",
        r"c:\Users\wtan\phd-optimacs\AA-all-repos\instances\knapsack-01\large_scale\knapPI_1_100_1000_1",
    ]

    for test_file in instances:
        print(f"\nParsing instance: {os.path.basename(test_file)}")
        instance = KnapsackInstance.parse_knapsack_file(test_file)
        instance.print()


if __name__ == "__main__":
    main()
