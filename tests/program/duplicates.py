from collections import Counter

class Duplicates:
    def __init__(self, arr):
        self.arr = arr

    def print_duplicates(self):
        element_counts = Counter(self.arr)
        duplicates = [item for item, count in element_counts.items() if count > 1]
        if duplicates:
            print("Duplicate elements:", duplicates)
        else:
            print("No duplicate elements found.")

# Example usage:
if __name__ == "__main__":
    # Sample input
    sample_array = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9]
    duplicates_finder = Duplicates(sample_array)
    duplicates_finder.print_duplicates()

