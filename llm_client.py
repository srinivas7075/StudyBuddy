# llm_client.py
from transformers import pipeline

class LLMClient:
    def __init__(self, model_name="gpt2"):
        """
        Initialize the Hugging Face text-generation pipeline.
        Default model: 'gpt2' (lightweight CPU-friendly).
        """
        self.pipeline = pipeline(
            "text-generation",
            model=model_name,
            device=-1  # -1 = CPU, 0 = GPU
        )

    def generate(self, prompt: str, max_tokens: int = 300):
        """
        Generate text based on the given prompt.
        Returns the generated string.
        """
        output = self.pipeline(prompt, max_new_tokens=max_tokens, do_sample=True, temperature=0.7)
        return output[0]["generated_text"]
