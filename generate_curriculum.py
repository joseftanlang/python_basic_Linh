from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class LessonSpec:
    number: int
    title: str
    goal: str
    challenge: str


LESSONS = [
    LessonSpec(1, "Introduction to Computing & Python", "Understand the input-process-output model and run a first Python program.", "a profile script that stores and prints variables"),
    LessonSpec(2, "Data Types", "Recognize int, float, str, and bool values and convert between them safely.", "a type-inspection worksheet for basic Python values"),
    LessonSpec(3, "Input and Output", "Collect user input and present clean output with f-strings.", "an input-driven calculator for personal measurements"),
    LessonSpec(4, "Operators", "Use arithmetic, comparison, and logical operators correctly.", "an operators drill that evaluates expressions and decisions"),
    LessonSpec(5, "Conditional Logic", "Write if, elif, and else branches that match real decisions.", "a grading and ticket-pricing decision tree"),
    LessonSpec(6, "Loops", "Use for and while loops to repeat tasks and count data.", "a loop worksheet that sums, filters, and repeats patterns"),
    LessonSpec(7, "Functions", "Break logic into reusable functions with parameters and return values.", "a reusable calculator toolkit built from small functions"),
    LessonSpec(8, "Lists", "Store ordered data and apply common list operations.", "a student marks manager built around list operations"),
    LessonSpec(9, "Dictionaries and Tuples", "Model labeled data with dictionaries and use tuples when values should stay fixed.", "a phone book and inventory lookup system"),
    LessonSpec(10, "Mini Project: Student Management System", "Combine variables, conditions, loops, functions, and collections into one interactive program.", "a student management mini project with search and score updates"),
    LessonSpec(11, "Strings Deep Dive", "Manipulate text with split, replace, strip, find, slicing, and formatting.", "a text-cleaning toolkit for names, messages, and notes"),
    LessonSpec(12, "Advanced Functions", "Use lambda, map, filter, and higher-order thinking to simplify repeated work.", "a functional-style data cleaner using lambda, map, and filter"),
    LessonSpec(13, "Error Handling", "Prevent crashes with try, except, finally, and raise.", "a safe input parser with clear error messages"),
    LessonSpec(14, "File Handling", "Read and write text, CSV, and JSON files in a structured way.", "a file workflow that stores and reloads lesson data"),
    LessonSpec(15, "Object-Oriented Programming Part 1", "Define classes, objects, and attributes to model real-world entities.", "a class-based student model with readable output"),
    LessonSpec(16, "OOP Part 2", "Use inheritance, polymorphism, and encapsulation to design reusable code.", "a school hierarchy that reuses a base class"),
    LessonSpec(17, "Modules and Packages", "Organize code across files and use import, pip, and venv with confidence.", "a small package layout with local imports"),
    LessonSpec(18, "Recursion", "Explain recursive calls, the call stack, and base cases.", "a recursion demo for factorial and Fibonacci"),
    LessonSpec(19, "Algorithm Basics", "Compare linear search and binary search and reason about complexity.", "an algorithm notebook that searches ordered and unordered data"),
    LessonSpec(20, "Project: Inventory Management System", "Build a larger program that combines collections, functions, files, and search.", "an inventory management project with file-backed storage"),
    LessonSpec(21, "NumPy Foundations", "Represent vectors and matrices efficiently and explain the basic NumPy mindset.", "a vector and matrix practice set using array thinking"),
    LessonSpec(22, "NumPy Advanced", "Use broadcasting, vectorization, and performance-aware array operations.", "a broadcasting exercise that replaces slow loops"),
    LessonSpec(23, "Pandas Foundations", "Load data into DataFrames and inspect rows, columns, and types.", "a CSV exploration notebook built around a DataFrame"),
    LessonSpec(24, "Data Cleaning", "Detect and fix missing values, duplicates, and obvious outliers.", "a cleaning pipeline for messy real-world data"),
    LessonSpec(25, "Data Transformation", "Group, aggregate, reshape, and summarize data for analysis.", "a transformation workflow using groupby and pivot tables"),
    LessonSpec(26, "Exploratory Data Analysis", "Use summary statistics and visualization to understand a dataset quickly.", "an EDA notebook that explains patterns and relationships"),
    LessonSpec(27, "Matplotlib", "Build clear charts with line, bar, scatter, and histogram plots.", "a plotting set that turns raw numbers into graphs"),
    LessonSpec(28, "Seaborn", "Create statistical visualizations that highlight comparisons and relationships.", "a Seaborn comparison set with heatmaps and pairplots"),
    LessonSpec(29, "Descriptive Statistics", "Compute mean, median, mode, variance, and standard deviation and interpret them.", "a descriptive statistics worksheet with worked calculations"),
    LessonSpec(30, "Probability Fundamentals", "Work with sample space, events, and conditional probability.", "a probability worksheet with event counting and intuition"),
    LessonSpec(31, "Probability Distributions", "Recognize normal, binomial, and Poisson distributions and when to use them.", "a distribution simulator for common probability models"),
    LessonSpec(32, "Hypothesis Testing", "Frame null and alternative hypotheses and interpret p-values and errors.", "a hypothesis testing worksheet with decision rules"),
    LessonSpec(33, "Confidence Intervals", "Build and interpret confidence intervals and margins of error.", "a confidence interval calculator for sample means"),
    LessonSpec(34, "Correlation vs Causation", "Compare Pearson and Spearman correlation and avoid causal mistakes.", "a correlation analysis that checks confounding variables"),
    LessonSpec(35, "Introduction to Machine Learning", "Explain supervised, unsupervised, and reinforcement learning and the ML workflow.", "a machine learning map that separates task types"),
    LessonSpec(36, "Data Preprocessing", "Prepare features with scaling, encoding, normalization, and feature engineering.", "a preprocessing pipeline for numeric and categorical data"),
    LessonSpec(37, "Linear Regression", "Connect cost functions, gradient descent, and prediction lines.", "a linear regression notebook with slope and error intuition"),
    LessonSpec(38, "Classification", "Use logistic regression ideas and decision boundaries for class prediction.", "a classification notebook with binary decision rules"),
    LessonSpec(39, "Decision Trees", "Explain entropy, information gain, and overfitting in tree models.", "a decision tree exercise that chooses splits step by step"),
    LessonSpec(40, "Random Forest", "Understand bagging, ensembling, and feature importance.", "a random forest comparison that explains why ensembles help"),
    LessonSpec(41, "Clustering", "Separate clustering from prediction and use K-means and hierarchical grouping.", "a clustering exercise that groups similar points"),
    LessonSpec(42, "Model Evaluation", "Measure performance with confusion matrix, precision, recall, F1, ROC-AUC, and cross-validation.", "a model evaluation worksheet with metric interpretation"),
    LessonSpec(43, "Neural Network Foundations", "Describe neurons, weights, bias, and activation functions.", "a neural network diagram that shows one forward pass"),
    LessonSpec(44, "Training Neural Networks", "Explain backpropagation, epochs, batch size, and learning rate.", "a training loop sketch that follows gradient updates"),
    LessonSpec(45, "TensorFlow / PyTorch", "Build, train, evaluate, and predict with a first deep learning model.", "a first framework-based model for tabular or toy data"),
    LessonSpec(46, "Computer Vision Basics", "Explain CNNs, image classification, and transfer learning.", "a CNN concept map for image understanding"),
    LessonSpec(47, "Introduction to LLMs", "Explain transformers, attention, tokens, embeddings, and GPT-style architectures.", "an LLM explainer for token flow and attention"),
    LessonSpec(48, "Prompt Engineering", "Use zero-shot, one-shot, few-shot, chain-of-thought, and evaluation habits.", "a prompt engineering workbook with quality checks"),
    LessonSpec(49, "RAG Systems", "Design retrieval-augmented generation with chunking, embeddings, vector search, and tools.", "a PDF question answering system plan with retrieval steps"),
    LessonSpec(50, "LLM Fine-Tuning & Capstone", "Connect fine-tuning, evaluation, deployment, and an end-to-end AI project.", "a capstone roadmap from raw data to deployed AI application"),
]


PHASES = {
    1: {
        "name": "Phase 1 - Python Programming Foundations",
        "summary": "Build syntax confidence, control flow, functions, and collection skills from zero.",
        "hour_1": [
            "Define the core idea for the lesson and connect it to the input-process-output model.",
            "Introduce the new syntax or data structure with a short worked example.",
            "Pause on each line so the student can predict the result before running code.",
        ],
        "hour_2": [
            "Solve the guided exercise with live coding and verbal reasoning.",
            "Add small variations so the student sees how the topic behaves under change.",
            "Point out beginner mistakes, naming rules, and debugging habits.",
        ],
        "hour_3": [
            "Work through three practice samples without copying the solution first.",
            "Refactor the result into smaller pieces or a reusable helper where possible.",
            "Close with a quick recap and a clear homework extension.",
        ],
        "homework": "Rebuild the main exercise from memory, change the input values, and explain the logic in plain English.",
        "self_practice": "Spend 45 minutes repeating the main task and 45 minutes extending it with new inputs or a small rule change.",
        "guided": [
            "trace the program step by step and predict each output",
            "check how the concept behaves when values or conditions change",
            "review one common beginner bug and how to fix it",
        ],
    },
    2: {
        "name": "Phase 2 - Intermediate Python",
        "summary": "Learn to organize code, handle errors, work with files, and think in reusable pieces.",
        "hour_1": [
            "Review the topic and relate it to code organization, safety, or reuse.",
            "Show a concise example that demonstrates the controlling concept.",
            "Explain why the topic matters in real scripts and projects.",
        ],
        "hour_2": [
            "Build the guided solution with helper functions or small structures.",
            "Add edge cases and validation to make the code more reliable.",
            "Discuss how the solution would scale in a larger project.",
        ],
        "hour_3": [
            "Practice with three exercises that increase in difficulty.",
            "Use the solution to compare control flow, data structure choice, or file format decisions.",
            "Wrap up with a refactor and one extension challenge.",
        ],
        "homework": "Rewrite the lesson exercise with your own data, then add one robustness improvement.",
        "self_practice": "Spend 1 hour rebuilding the exercise and 1 hour improving the design, error handling, or reuse.",
        "guided": [
            "show how the topic improves readability or reliability",
            "work through one complete example and one failure case",
            "explain the trade-off between the quick solution and the reusable solution",
        ],
    },
    3: {
        "name": "Phase 3 - Python for Data Analysis",
        "summary": "Use arrays, tables, cleaning steps, and charts to understand real datasets.",
        "hour_1": [
            "Introduce the data-analysis problem and define the shape of the data.",
            "Walk through the core library objects or operations used in the lesson.",
            "Show how to inspect data before changing it.",
        ],
        "hour_2": [
            "Load a dataset or create a realistic sample and explore its structure.",
            "Perform the key transformation or cleanup step for the lesson.",
            "Explain how the result helps analysis or reporting.",
        ],
        "hour_3": [
            "Complete three short tasks that mimic a real analysis workflow.",
            "Check output quality, missing values, types, or chart readability.",
            "Summarize the lesson with one reproducible analysis habit.",
        ],
        "homework": "Repeat the data workflow on a second dataset and write down what changed.",
        "self_practice": "Spend 30 minutes repeating the workflow and 60 minutes comparing two different datasets or charts.",
        "guided": [
            "inspect the data first, then change it intentionally",
            "connect every transformation to a question the data should answer",
            "look for shape, type, or distribution issues before moving on",
        ],
    },
    4: {
        "name": "Phase 4 - Statistics for Data Science",
        "summary": "Build statistical reasoning so model results and data patterns can be interpreted correctly.",
        "hour_1": [
            "Define the statistical idea and connect it to everyday interpretation.",
            "Work through the formula or concept with a small sample by hand.",
            "Translate the numbers into a plain-language conclusion.",
        ],
        "hour_2": [
            "Use code or a calculator to automate the repeated statistical step.",
            "Check the assumptions and limits of the result.",
            "Compare a correct interpretation with a common misunderstanding.",
        ],
        "hour_3": [
            "Solve three interpretation tasks using the same statistical idea.",
            "Discuss when the statistic is useful and when it is misleading.",
            "Finish with a short written explanation of the result.",
        ],
        "homework": "Compute the same statistic on a different dataset and explain what changes.",
        "self_practice": "Spend 1 hour solving by hand and 1 hour checking your work with code or a calculator.",
        "guided": [
            "show the math, then show the meaning of the number",
            "separate calculation errors from interpretation errors",
            "link each statistic to a decision or claim about the data",
        ],
    },
    5: {
        "name": "Phase 5 - Machine Learning Foundations",
        "summary": "Prepare data, train baseline models, and evaluate predictions with discipline.",
        "hour_1": [
            "Introduce the learning task and define the target, features, and baseline.",
            "Explain the model idea with a simple geometric or mathematical picture.",
            "Show how the lesson fits into the full ML pipeline.",
        ],
        "hour_2": [
            "Prepare the data and run a baseline model or algorithm.",
            "Inspect predictions, mistakes, and the reason the model behaves that way.",
            "Discuss overfitting, underfitting, and the role of validation.",
        ],
        "hour_3": [
            "Complete three practice problems that reinforce the full workflow.",
            "Evaluate the result using a metric that matches the task.",
            "Close with one improvement idea for the next iteration.",
        ],
        "homework": "Repeat the modeling workflow with a different split, feature set, or algorithm.",
        "self_practice": "Spend 1 hour on the workflow and 1 hour on evaluation, error analysis, or improvement.",
        "guided": [
            "keep the full pipeline visible from data to metric",
            "explain why a metric is chosen instead of just computing it",
            "compare baseline, improvement, and failure cases",
        ],
    },
    6: {
        "name": "Phase 6 - Deep Learning",
        "summary": "Understand neural networks as trainable function approximators and learn how they are optimized.",
        "hour_1": [
            "Introduce the network building blocks and how information flows through them.",
            "Work through one neuron or layer by hand.",
            "Explain why activation functions matter.",
        ],
        "hour_2": [
            "Show training, loss, and gradient updates in a small example.",
            "Discuss batch size, epochs, and learning rate in practical terms.",
            "Connect the math to the implementation used in the lesson.",
        ],
        "hour_3": [
            "Practice by tracing a forward pass and one training step.",
            "Inspect a common training failure and how to fix it.",
            "Summarize what deep learning adds beyond classical ML.",
        ],
        "homework": "Draw the network or training loop from memory and explain each step in words.",
        "self_practice": "Spend 45 minutes tracing the math and 45 minutes reviewing a training example or diagram.",
        "guided": [
            "connect the equations to the forward and backward passes",
            "show how training changes the network over time",
            "compare a healthy training run with a broken one",
        ],
    },
    7: {
        "name": "Phase 7 - LLM Engineering and Generative AI",
        "summary": "Build the mental model for modern LLM systems, prompting, retrieval, and deployment.",
        "hour_1": [
            "Explain the model architecture or system concept at a high level.",
            "Walk through tokens, embeddings, retrieval, or attention with a simple example.",
            "Show how the lesson supports real AI application design.",
        ],
        "hour_2": [
            "Prototype the core workflow in code or pseudocode.",
            "Discuss safety, evaluation, cost, and quality trade-offs.",
            "Show how to improve the system in a measurable way.",
        ],
        "hour_3": [
            "Practice with three design or implementation tasks.",
            "Review failure modes such as hallucination, weak retrieval, or prompt drift.",
            "End with a capstone-style reflection or system design note.",
        ],
        "homework": "Write a one-page design note that explains the lesson idea and how you would use it in an app.",
        "self_practice": "Spend 1 hour writing or improving a prototype and 1 hour evaluating quality, cost, or safety.",
        "guided": [
            "show how the AI system is assembled end to end",
            "connect model behavior to prompt, data, and retrieval choices",
            "name the main failure mode and the way to measure it",
        ],
    },
}


def phase_for(number: int) -> int:
    if number <= 10:
        return 1
    if number <= 20:
        return 2
    if number <= 28:
        return 3
    if number <= 34:
        return 4
    if number <= 42:
        return 5
    if number <= 46:
        return 6
    return 7


def phase_label(number: int) -> str:
    return PHASES[phase_for(number)]["name"]


def kind_for(number: int) -> str:
    if number <= 4:
        return "syntax"
    if number <= 7:
        return "control"
    if number <= 10:
        return "collections"
    if number <= 14:
        return "strings_files"
    if number <= 16:
        return "oop"
    if number <= 20:
        return "algorithms"
    if number <= 22:
        return "numpy"
    if number <= 26:
        return "pandas"
    if number <= 28:
        return "viz"
    if number <= 34:
        return "statistics"
    if number <= 42:
        return "ml"
    if number <= 46:
        return "dl"
    return "llm"


def lesson_dir(number: int) -> Path:
    return ROOT / f"lesson-{number:03d}"


def readme_text(spec: LessonSpec) -> str:
    phase = PHASES[phase_for(spec.number)]
    guided = "\n".join(f"- {line}" for line in phase["guided"])
    hour_1 = "\n".join(f"- {line}" for line in phase["hour_1"])
    hour_2 = "\n".join(f"- {line}" for line in phase["hour_2"])
    hour_3 = "\n".join(f"- {line}" for line in phase["hour_3"])
    return dedent(
        f"""
        # Lesson {spec.number:03d} - {spec.title}

        {phase['name']}

        Duration: 3 hours

        Overview
        - {spec.goal}
        - {phase['summary']}
        - The session focuses on one clear topic, three guided practice tasks, and a short homework extension.

        Learning outcomes
        - Explain the main idea of {spec.title.lower()} in simple language.
        - Solve the core exercise for this lesson without relying on memorization alone.
        - Connect the topic to the next lesson so the student keeps building a full workflow.

        3-hour plan
        Hour 1
        {hour_1}

        Hour 2
        {hour_2}

        Hour 3
        {hour_3}

        Guided examples
        {guided}

        Practice samples
        1. {spec.challenge}
        2. Extend the same idea with validation, edge cases, or richer output so the student must think through the rules.
        3. Turn the exercise into a reusable helper, small module, notebook cell, or mini project depending on the topic.

        Homework
        - {phase['homework']}
        - Save one mistake, one fix, and one takeaway in your own study notes.

        Self-practice
        - {phase['self_practice']}
        - If the topic feels easy, repeat it with new values or a larger dataset instead of moving on immediately.

        Key habits
        - Predict the result before running the code.
        - Read errors carefully and fix one issue at a time.
        - Refactor only after the first working version is complete.
        """
    ).strip() + "\n"


def solution_text(spec: LessonSpec) -> str:
    kind = kind_for(spec.number)
    title = spec.title

    if kind == "syntax":
        body = f'''
        def demo_greeting():
            return "Hello, World!"


        def demo_profile():
            profile = {{"name": "Josef", "age": 20, "country": "Vietnam"}}
            return f"{{profile['name']}} is {{profile['age']}} years old and lives in {{profile['country']}}."


        def demo_memory_story():
            variable_name = "name"
            value = "Linh"
            return f"A variable named {{variable_name}} can store {{value}}."


        def demo():
            print(demo_greeting())
            print(demo_profile())
            print(demo_memory_story())


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "control":
        body = f'''
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
        '''
    elif kind == "collections":
        body = f'''
        def add_student(students: list[dict], name: str, score: float) -> list[dict]:
            students.append({{"name": name, "score": score}})
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
            print(phone_lookup({{"Ana": "0901-111-222"}}, "Ana"))
            print(inventory_adjust({{"pens": 10}}, "pens", 5))


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "strings_files":
        body = f'''
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
        '''
    elif kind == "oop":
        body = f'''
        class Student:
            def __init__(self, name: str, age: int, score: float):
                self.name = name
                self.age = age
                self.score = score

            def average_label(self) -> str:
                return f"{{self.name}} has a score of {{self.score:.1f}}"


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
        '''
    elif kind == "algorithms":
        body = f'''
        def linear_search(values: list[int], target: int) -> int:
            for index, value in enumerate(values):
                if value == target:
                    return index
            return -1


        def binary_search(values: list[int], target: int) -> int:
            left, right = 0, len(values) - 1
            while left <= right:
                mid = (left + right) // 2
                if values[mid] == target:
                    return mid
                if values[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1


        def inventory_update(stock: dict[str, int], item: str, quantity: int) -> dict[str, int]:
            stock[item] = stock.get(item, 0) + quantity
            return stock


        def demo():
            numbers = [2, 4, 6, 8, 10, 12]
            print(linear_search(numbers, 8))
            print(binary_search(numbers, 10))
            print(inventory_update({{"markers": 3}}, "markers", 2))


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "numpy":
        body = f'''
        try:
            import numpy as np
        except ImportError:  # pragma: no cover - optional dependency
            np = None


        def vector_add(values_a, values_b):
            if np is not None:
                return np.array(values_a) + np.array(values_b)
            return [a + b for a, b in zip(values_a, values_b)]


        def matrix_mean(matrix):
            if np is not None:
                return float(np.array(matrix).mean())
            flat = [value for row in matrix for value in row]
            return sum(flat) / len(flat)


        def normalize(values):
            if np is not None:
                arr = np.array(values, dtype=float)
                return (arr - arr.min()) / (arr.max() - arr.min()) if arr.max() != arr.min() else arr
            minimum = min(values)
            maximum = max(values)
            if maximum == minimum:
                return [0.0 for _ in values]
            return [(value - minimum) / (maximum - minimum) for value in values]


        def demo():
            print(vector_add([1, 2, 3], [4, 5, 6]))
            print(matrix_mean([[1, 2], [3, 4]]))
            print(normalize([10, 20, 30]))


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "pandas":
        body = f'''
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
            summary = {{}}
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
                {{"region": "North", "sales": 120}},
                {{"region": "South", "sales": 150}},
                {{"region": "North", "sales": 80}},
            ]
            print(make_table(rows))
            print(summarize_sales(rows))
            print(fill_missing([1, None, 3], 0))


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "viz":
        body = f'''
        try:
            import matplotlib.pyplot as plt
        except ImportError:  # pragma: no cover - optional dependency
            plt = None


        def line_plot_data(values):
            if plt is None:
                return {{"type": "line", "values": values}}
            fig, ax = plt.subplots()
            ax.plot(values)
            ax.set_title("Line Plot")
            return fig


        def bar_plot_data(labels, values):
            if plt is None:
                return {{"type": "bar", "labels": labels, "values": values}}
            fig, ax = plt.subplots()
            ax.bar(labels, values)
            ax.set_title("Bar Chart")
            return fig


        def histogram_data(values):
            if plt is None:
                return {{"type": "histogram", "values": values}}
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
        '''
    elif kind == "statistics":
        body = f'''
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
        '''
    elif kind == "ml":
        body = f'''
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
            return {{"tp": tp, "tn": tn, "fp": fp, "fn": fn}}


        def demo():
            rows = [1, 2, 3, 4, 5, 6]
            print(train_test_split_simple(rows))
            print(linear_prediction(2.5, 1.0, 4))
            print(confusion_counts([1, 0, 1, 0], [1, 0, 0, 0]))


        if __name__ == "__main__":
            demo()
        '''
    elif kind == "dl":
        body = f'''
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
        '''
    else:  # llm
        body = f'''
        from math import sqrt


        def simple_tokenize(text: str):
            return [token for token in text.lower().replace("\n", " ").split() if token]


        def build_prompt(system: str, question: str) -> str:
            return f"System: {{system}}\nUser: {{question}}\nAssistant:"


        def chunk_text(text: str, chunk_size: int = 40):
            words = text.split()
            return [" ".join(words[index:index + chunk_size]) for index in range(0, len(words), chunk_size)]


        def cosine_similarity(values_a, values_b):
            dot_product = sum(a * b for a, b in zip(values_a, values_b))
            magnitude_a = sqrt(sum(a * a for a in values_a))
            magnitude_b = sqrt(sum(b * b for b in values_b))
            if magnitude_a == 0 or magnitude_b == 0:
                return 0.0
            return dot_product / (magnitude_a * magnitude_b)


        def demo():
            print(simple_tokenize("Attention is about focused context."))
            print(build_prompt("Be concise.", "Explain embeddings."))
            print(chunk_text("This lesson shows how to split a document into smaller overlapping sections for retrieval."))
            print(cosine_similarity([1, 2, 3], [2, 3, 4]))


        if __name__ == "__main__":
            demo()
        '''

    return dedent(
        f'''"""Lesson {spec.number:03d}: {title}

        Example solutions aligned to the three practice samples in the lesson README.
        """
        {body}
        '''
    ).strip() + "\n"


def top_level_readme() -> str:
    return dedent(
        """
        # Python -> Data Science -> Machine Learning -> LLM Engineering

        This repository now follows a 50-lesson curriculum with 3 hours per lesson for a total of 150 hours.

        Curriculum map
        - Lessons 1-10: Python Programming Foundations
        - Lessons 11-20: Intermediate Python
        - Lessons 21-28: Python for Data Analysis
        - Lessons 29-34: Statistics for Data Science
        - Lessons 35-42: Machine Learning Foundations
        - Lessons 43-46: Deep Learning
        - Lessons 47-50: LLM Engineering and Generative AI

        How the lessons are organized
        - Each lesson folder contains a detailed README with outcomes, a 3-hour plan, guided examples, three practice samples, homework, and self-practice guidance.
        - Each lesson folder also contains a separate solutions.py file with sample implementations for the practice work.
        - Follow the folders in order. The course is designed for a student starting from zero and steadily moving toward building AI applications.

        How to use the repository
        - Open lesson-001 and work sequentially through lesson-050.
        - Run python all_solutions.py to preview the solution demos for the active curriculum.
        - Treat the older lesson-051 to lesson-060 folders as legacy material outside the new 50-lesson path.

        Suggested study routine
        - Read the README first.
        - Code along with the guided examples.
        - Attempt the three practice samples before checking the solutions.
        - Revisit the homework and self-practice section after class.

        Outcome
        - By lesson 50, the student should be able to write Python confidently, analyze data, reason statistically, train baseline machine learning models, understand deep learning fundamentals, and design practical LLM applications.
        """
    ).strip() + "\n"


def all_solutions_text() -> str:
    return dedent(
        """
        from __future__ import annotations

        from pathlib import Path
        import runpy


        ROOT = Path(__file__).resolve().parent


        def main() -> None:
            for number in range(1, 51):
                lesson_dir = ROOT / f"lesson-{number:03d}"
                solution_file = lesson_dir / "solutions.py"
                if not solution_file.exists():
                    continue
                print(f"--- lesson-{number:03d} ---")
                namespace = runpy.run_path(str(solution_file))
                demo = namespace.get("demo")
                if callable(demo):
                    demo()
                else:
                    print("No demo() found.")


        if __name__ == "__main__":
            main()
        """
    ).strip() + "\n"


def write_curriculum() -> None:
    (ROOT / "README.md").write_text(top_level_readme(), encoding="utf-8")
    (ROOT / "all_solutions.py").write_text(all_solutions_text(), encoding="utf-8")

    for spec in LESSONS:
        directory = lesson_dir(spec.number)
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "README.md").write_text(readme_text(spec), encoding="utf-8")
        (directory / "solutions.py").write_text(solution_text(spec), encoding="utf-8")


if __name__ == "__main__":
    write_curriculum()
