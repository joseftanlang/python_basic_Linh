"""Lesson 050: LLM Fine-Tuning & Capstone

        Example solutions aligned to the three practice samples in the lesson README.
        """

        from math import sqrt


        def simple_tokenize(text: str):
            return [token for token in text.lower().replace("
", " ").split() if token]


        def build_prompt(system: str, question: str) -> str:
            return f"System: {system}
User: {question}
Assistant:"


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
