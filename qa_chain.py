import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please set it in your .env file.")

class QAChain:

    def __init__(self, openai_model="gpt-3.5-turbo", max_context_chars=2000):
        self.llm = OpenAI(openai_api_key=OPENAI_API_KEY, model_name=openai_model)
        self.max_context_chars = max_context_chars

    def generate_answer(self, question, context_chunks):
        combined_context = "\n\n---\n\n".join(context_chunks)

        if len(combined_context) > self.max_context_chars:
            combined_context = combined_context[:self.max_context_chars]

        prompt = f"""
Use ONLY the following context to answer the user question. If the answer is not contained in the context, say "I don't know".

Context:
{combined_context}

Question: {question}

Answer:
"""

        response = self.llm(prompt)
        return response.strip()
