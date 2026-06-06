"""Lesson 015: Object-Oriented Programming Part 1

        Example solutions aligned to the three practice samples in the lesson README.
        """

        class Student:
            def __init__(self, name: str, age: int, score: float):
                self.name = name
                self.age = age
                self.score = score

            def average_label(self) -> str:
                return f"{self.name} has a score of {self.score:.1f}"


        class Course:
            def __init__(self, title: str):
                self.title = title
                self.students = []

            def add_student(self, student: Student) -> None:
                self.students.append(student)

            def average_score(self) -> float:
                if not self.students:
                    return 0.0
                return sum(student.score for student in self.students) / len(self.students)


        def demo():
            course = Course("Python Basics")
            course.add_student(Student("Ana", 20, 91.5))
            course.add_student(Student("Bob", 21, 84.0))
            print(course.average_score())
            print(course.students[0].average_label())


        if __name__ == "__main__":
            demo()
