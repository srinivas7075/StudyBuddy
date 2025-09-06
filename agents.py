# agents.py

from llm_client import LLMClient

class PlannerAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def make_plan(self, topic: str, hours: int = 2):
        """
        Generates a concise study plan.
        Format strictly as:
        Session X: Title (Y minutes) - Objective 1 - Objective 2 - Objective 3
        """
        prompt = (
            f"Create a concise {hours}-hour study plan for '{topic}'. "
            "Break it into 3-5 sessions. "
            "Output strictly in this format:\n"
            "Session X: Title (Y minutes) - Objective 1 - Objective 2 - Objective 3\n"
            "Do not repeat, do not add explanations."
        )
        return self.llm.generate(prompt)


class SummarizerAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def summarize(self, session_text: str):
        """
        Summarizes a single study session in 3-4 bullet points.
        """
        prompt = (
            f"Summarize the following study session in 3-4 clear bullet points:\n\n{session_text}"
        )
        return self.llm.generate(prompt)


class QuizAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def generate_quiz(self, topic: str, n_questions: int = 3):
        """
        Generates multiple-choice questions (A-D) for a topic.
        Each question includes the correct answer.
        """
        prompt = (
            f"Generate {n_questions} multiple-choice questions (A-D) for '{topic}'. "
            "Include the correct answer after each question. Keep it concise."
        )
        return self.llm.generate(prompt)
