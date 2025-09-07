# StudyBuddy — Multi-Agent Study Planner

## 📌 Problem Statement
Students often struggle to organize their study time effectively. They need structured study plans, concise summaries, and quick self-check quizzes to prepare better.  
This project builds **StudyBuddy**, a simple **AI multi-agent system** that helps students create study plans, generate summaries, and practice quizzes for any topic.

## 🤖 Why Multi-Agent?
Instead of one big model doing everything, we divide responsibilities across agents:
- **Planner Agent**: creates a study plan session by session.
- **Summarizer Agent**: generates short bullet-point summaries of content.
- **Quiz Agent**: makes small multiple-choice quizzes.  
This shows how agents can work **independently** and then **collaborate** through an orchestrator script.

## 🛠 Tools, Libraries, and Frameworks
- **Python 3.10+**
- **OpenAI GPT-3.5-turbo** (main LLM, via `openai` library)  
- **Hugging Face flan-t5-small** (free fallback model, via `transformers`)  
- **Optional**: Streamlit (for demo UI)  

## 🔎 LLM Selection
- **Ideal LLM**: GPT-4 (better quality reasoning, but paid).  
- **Chosen**: GPT-3.5-turbo (fast, affordable, works well).  
- **Free option**: Hugging Face `flan-t5-small` — works without cost, but simpler output.  

## 🚀 How it Works
1. User enters a **topic** (e.g., "Operating Systems basics") and available **study hours**.  
2. **Planner Agent** makes a structured study plan.  
3. **Summarizer Agent** converts each session into quick bullet notes.  
4. **Quiz Agent** generates MCQs for practice.  
5. Orchestrator (`main.py`) coordinates agents and displays results.

## 📂 Project Structure
```bash
StudyBuddy/
├── agents.py # Defines Planner, Summarizer, and Quiz Agents
├── llm_client.py # Handles LLM calls (OpenAI/HuggingFace)
├── main.py # Orchestrator that coordinates all agents
├── requirements.txt # Project dependencies
├── README.md # Documentation
└── venv/ # Virtual environment (ignored by git)
```
