"""Lesson 028: Seaborn

        Example solutions aligned to the three practice samples in the lesson README.
        """

        try:
            import matplotlib.pyplot as plt
        except ImportError:  # pragma: no cover - optional dependency
            plt = None


        def line_plot_data(values):
            if plt is None:
                return {"type": "line", "values": values}
            fig, ax = plt.subplots()
            ax.plot(values)
            ax.set_title("Line Plot")
            return fig


        def bar_plot_data(labels, values):
            if plt is None:
                return {"type": "bar", "labels": labels, "values": values}
            fig, ax = plt.subplots()
            ax.bar(labels, values)
            ax.set_title("Bar Chart")
            return fig


        def histogram_data(values):
            if plt is None:
                return {"type": "histogram", "values": values}
            fig, ax = plt.subplots()
            ax.hist(values, bins=5)
            ax.set_title("Histogram")
            return fig


        def demo():
            print(line_plot_data([1, 3, 2, 5]))
            print(bar_plot_data(["A", "B", "C"], [4, 7, 2]))
            print(histogram_data([1, 1, 2, 3, 5, 8]))


        if __name__ == "__main__":
            demo()
