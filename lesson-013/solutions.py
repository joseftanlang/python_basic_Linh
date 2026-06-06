"""Lesson 013: Error Handling

        Example solutions aligned to the three practice samples in the lesson README.
        """

        from pathlib import Path


        def clean_text(text: str) -> str:
            return " ".join(text.strip().split()).lower()


        def count_words(text: str) -> int:
            return len(clean_text(text).split()) if clean_text(text) else 0


        def write_report(path: str, text: str) -> str:
            output = Path(path)
            output.write_text(text, encoding="utf-8")
            return str(output)


        def demo():
            sample = "  Python   is  powerful and clear.  "
            print(clean_text(sample))
            print(count_words(sample))
            print(write_report("demo_report.txt", sample))


        if __name__ == "__main__":
            demo()
