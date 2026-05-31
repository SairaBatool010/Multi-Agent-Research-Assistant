import requests

class OllamaLLM:
    def __init__(self, model="llama3.2:3b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]