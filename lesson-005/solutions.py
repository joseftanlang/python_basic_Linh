"""Lesson 005: Conditional Logic

        Example solutions aligned to the three practice samples in the lesson README.
        """

        def grade_score(score: int) -> str:
            if score >= 90:
                return "A"
            if score >= 80:
                return "B"
            if score >= 70:
                return "C"
            if score >= 60:
                return "D"
            return "F"


        def ticket_price(age: int, student: bool = False) -> int:
            price = 120
            if age < 12:
                price = 60
            elif age >= 60:
                price = 70
            if student:
                price -= 20
            return max(price, 0)


        def login_allowed(username: str, password: str) -> bool:
            return bool(username.strip()) and len(password) >= 6


        def demo():
            print(grade_score(84))
            print(ticket_price(15, student=True))
            print(login_allowed("student", "secret7"))


        if __name__ == "__main__":
            demo()
