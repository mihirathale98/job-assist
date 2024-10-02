import os
from together import Together


class TogetherModel:
    def __init__(self):
        self.client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

    def generate(self, text, model='meta-llama/Llama-3.2-3B-Instruct-Turbo'):
        response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": text}],
                )
        
        return response.choices[0].message.content
                        
