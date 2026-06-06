"""Lesson 003: Input and Output

        Example solutions aligned to the three practice samples in the lesson README.
        """

        def demo_greeting():
            return "Hello, World!"


        def demo_profile():
            profile = {"name": "Josef", "age": 20, "country": "Vietnam"}
            return f"{profile['name']} is {profile['age']} years old and lives in {profile['country']}."


        def demo_memory_story():
            variable_name = "name"
            value = "Linh"
            return f"A variable named {variable_name} can store {value}."


        def demo():
            print(demo_greeting())
            print(demo_profile())
            print(demo_memory_story())


        if __name__ == "__main__":
            demo()
