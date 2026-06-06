"""Lesson 022: NumPy Advanced

        Example solutions aligned to the three practice samples in the lesson README.
        """

        try:
            import numpy as np
        except ImportError:  # pragma: no cover - optional dependency
            np = None


        def vector_add(values_a, values_b):
            if np is not None:
                return np.array(values_a) + np.array(values_b)
            return [a + b for a, b in zip(values_a, values_b)]


        def matrix_mean(matrix):
            if np is not None:
                return float(np.array(matrix).mean())
            flat = [value for row in matrix for value in row]
            return sum(flat) / len(flat)


        def normalize(values):
            if np is not None:
                arr = np.array(values, dtype=float)
                return (arr - arr.min()) / (arr.max() - arr.min()) if arr.max() != arr.min() else arr
            minimum = min(values)
            maximum = max(values)
            if maximum == minimum:
                return [0.0 for _ in values]
            return [(value - minimum) / (maximum - minimum) for value in values]


        def demo():
            print(vector_add([1, 2, 3], [4, 5, 6]))
            print(matrix_mean([[1, 2], [3, 4]]))
            print(normalize([10, 20, 30]))


        if __name__ == "__main__":
            demo()
