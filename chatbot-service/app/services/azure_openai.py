# Azure OpenAI Service
import os
import openai

class AzureOpenAIService:
    def __init__(self, api_key, engine):
        self.api_key = api_key
        self.engine = engine
        openai.api_key = self.api_key

    async def generate_response(self, message: str, context: str) -> str:
        prompt = f"{context}\n\n{message}"
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()