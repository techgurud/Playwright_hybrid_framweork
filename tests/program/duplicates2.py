class Duplicates2:
    def __init__(self,arr):
        self.arr =arr

    def find_duplicates(arr):
        seen = set()
        return [num for num in arr if num in seen or seen.add(num)]
    
    if __name__ == "__main__":
        # Sample input
        sample_array = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9]
        print(find_duplicates(sample_array))
        