"""Lesson 033: Confidence Intervals

        Example solutions aligned to the three practice samples in the lesson README.
        """

        from math import sqrt


        def mean(values):
            return sum(values) / len(values)


        def median(values):
            ordered = sorted(values)
            middle = len(ordered) // 2
            if len(ordered) % 2:
                return ordered[middle]
            return (ordered[middle - 1] + ordered[middle]) / 2


        def sample_std(values):
            avg = mean(values)
            variance = sum((value - avg) ** 2 for value in values) / (len(values) - 1)
            return sqrt(variance)


        def demo():
            values = [2, 4, 4, 4, 5, 5, 7, 9]
            print(mean(values))
            print(median(values))
            print(sample_std(values))


        if __name__ == "__main__":
            demo()
