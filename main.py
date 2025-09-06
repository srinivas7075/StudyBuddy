# main.py
from llm_client import LLMClient
from agents import PlannerAgent, SummarizerAgent, QuizAgent

def main():
    # Initialize LLM
    llm = LLMClient()
    
    # Initialize agents
    planner = PlannerAgent(llm)
    summarizer = SummarizerAgent(llm)
    quizzer = QuizAgent(llm)
    
    # User input
    topic = input("Enter study topic (e.g. 'Operating Systems basics'): ").strip()
    hours_input = input("Study hours (default 2): ").strip()
    hours = int(hours_input) if hours_input.isdigit() else 2

    # Generate study plan
    print("\nGenerating study plan...\n")
    plan = planner.make_plan(topic, hours)
    print("--- Study Plan ---\n")
    print(plan)

    # Summarize first 3 sessions (assuming split by 'Session')
    sessions = [s for s in plan.split("Session") if s.strip()]
    print("\nGenerating session summaries and quizzes (first 3 sessions)...\n")
    for i, session in enumerate(sessions[:3], 1):
        session_text = "Session" + session.strip()
        summary = summarizer.summarize(session_text)
        quiz = quizzer.generate_quiz(topic)
        print(f"Session {i} Summary:\n{summary}\n")
        print(f"Quiz:\n{quiz}\n")
        print("="*50)

if __name__ == "__main__":
    main()
