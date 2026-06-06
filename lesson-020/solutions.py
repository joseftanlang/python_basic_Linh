"""Lesson 020: Project: Inventory Management System

        Example solutions aligned to the three practice samples in the lesson README.
        """

        def linear_search(values: list[int], target: int) -> int:
            for index, value in enumerate(values):
                if value == target:
                    return index
            return -1


        def binary_search(values: list[int], target: int) -> int:
            left, right = 0, len(values) - 1
            while left <= right:
                mid = (left + right) // 2
                if values[mid] == target:
                    return mid
                if values[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1


        def inventory_update(stock: dict[str, int], item: str, quantity: int) -> dict[str, int]:
            stock[item] = stock.get(item, 0) + quantity
            return stock


        def demo():
            numbers = [2, 4, 6, 8, 10, 12]
            print(linear_search(numbers, 8))
            print(binary_search(numbers, 10))
            print(inventory_update({"markers": 3}, "markers", 2))


        if __name__ == "__main__":
            demo()
