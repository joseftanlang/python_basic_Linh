"""Lesson 037: Linear Regression

        Example solutions aligned to the three practice samples in the lesson README.
        """

        from math import exp


        def train_test_split_simple(rows, test_size=0.25):
            split_index = max(1, int(len(rows) * (1 - test_size)))
            return rows[:split_index], rows[split_index:]


        def linear_prediction(weight, bias, x_value):
            return weight * x_value + bias


        def confusion_counts(actual, predicted):
            tp = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 1)
            tn = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 0)
            fp = sum(1 for a, p in zip(actual, predicted) if a == 0 and p == 1)
            fn = sum(1 for a, p in zip(actual, predicted) if a == 1 and p == 0)
            return {"tp": tp, "tn": tn, "fp": fp, "fn": fn}


        def demo():
            rows = [1, 2, 3, 4, 5, 6]
            print(train_test_split_simple(rows))
            print(linear_prediction(2.5, 1.0, 4))
            print(confusion_counts([1, 0, 1, 0], [1, 0, 0, 0]))


        if __name__ == "__main__":
            demo()
