import os
import dotenv
import openai

# Load environment variables
dotenv.load_dotenv()

# Azure OpenAI configuration
AZURE_OPENAI_SERVICE = os.getenv("AZURE_OPENAI_SERVICE")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


class AzureOpenAIClient:
    def __init__(self):
        self.client = openai.AzureOpenAI(
            api_version="2023-07-01-preview",
            azure_endpoint=f"https://{AZURE_OPENAI_SERVICE}.openai.azure.com"
        )

    def get_embedding(self, text):
        """
        Generate embeddings for given text

        :param text: Input text to generate embedding for
        :return: Embedding vector
        """
        get_embeddings_response = self.client.embeddings.create(
            model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
            input=text
        )
        return get_embeddings_response.data[0].embedding

    def generate_response(self, messages):
        """
        Generate a response using Azure OpenAI

        :param messages: List of message dictionaries
        :return: Generated response
        """
        response = self.client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=messages
        )
        return response.choices[0].message.content
