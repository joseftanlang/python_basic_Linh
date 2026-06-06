"""Lesson 045: TensorFlow / PyTorch

        Example solutions aligned to the three practice samples in the lesson README.
        """

        from math import exp


        def relu(value):
            return max(0.0, value)


        def dense_forward(inputs, weights, bias):
            return sum(input_value * weight for input_value, weight in zip(inputs, weights)) + bias


        def softmax(values):
            exps = [exp(value) for value in values]
            total = sum(exps)
            return [value / total for value in exps]


        def demo():
            print(relu(-3.5))
            print(dense_forward([1.0, 2.0], [0.4, 0.6], 0.1))
            print(softmax([1.0, 2.0, 3.0]))


        if __name__ == "__main__":
            demo()
