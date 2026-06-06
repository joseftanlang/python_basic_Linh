"""Lesson 009: Dictionaries and Tuples

        Example solutions aligned to the three practice samples in the lesson README.
        """

        def add_student(students: list[dict], name: str, score: float) -> list[dict]:
            students.append({"name": name, "score": score})
            return students


        def phone_lookup(book: dict[str, str], name: str) -> str:
            return book.get(name, "Not found")


        def inventory_adjust(stock: dict[str, int], item: str, quantity: int) -> dict[str, int]:
            stock[item] = stock.get(item, 0) + quantity
            return stock


        def demo():
            students = []
            add_student(students, "Ana", 92)
            add_student(students, "Bob", 87)
            print(students)
            print(phone_lookup({"Ana": "0901-111-222"}, "Ana"))
            print(inventory_adjust({"pens": 10}, "pens", 5))


        if __name__ == "__main__":
            demo()
