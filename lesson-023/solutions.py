"""Lesson 023: Pandas Foundations

        Example solutions aligned to the three practice samples in the lesson README.
        """

        try:
            import pandas as pd
        except ImportError:  # pragma: no cover - optional dependency
            pd = None


        def make_table(rows):
            if pd is not None:
                return pd.DataFrame(rows)
            return rows


        def summarize_sales(rows):
            if pd is not None:
                frame = pd.DataFrame(rows)
                return frame.groupby("region", as_index=False)["sales"].sum()
            summary = {}
            for row in rows:
                summary[row["region"]] = summary.get(row["region"], 0) + row["sales"]
            return summary


        def fill_missing(values, default):
            if pd is not None:
                series = pd.Series(values)
                return series.fillna(default)
            return [default if value is None else value for value in values]


        def demo():
            rows = [
                {"region": "North", "sales": 120},
                {"region": "South", "sales": 150},
                {"region": "North", "sales": 80},
            ]
            print(make_table(rows))
            print(summarize_sales(rows))
            print(fill_missing([1, None, 3], 0))


        if __name__ == "__main__":
            demo()
