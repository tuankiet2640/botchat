from azure_openai import AzureOpenAIClient
from azure_ai_search import AzureAISearchClient
from typing import List, Optional


class ChatOrchestrator:
    def __init__(self):
        self.openai_client = AzureOpenAIClient()
        self.search_client = AzureAISearchClient()

    def process_query(
            self,
            user_question: str,
            chat_history: Optional[List[dict]] = None
    ) -> str:
        """
        Process user query with optional chat history

        :param user_question: User's input query
        :param chat_history: Optional list of previous messages
        :return: AI-generated response
        """
        # Perform semantic search to get relevant sources
        search_results = self.search_client.search(
            user_question,
            embedding_func=self.openai_client.get_embedding
        )

        # Prepare messages for context-aware response
        messages = []

        # Add system context
        messages.append({
            "role": "system",
            "content": "You are a helpful AI assistant. Use the provided context to answer questions precisely."
        })

        # Add previous chat history if provided
        if chat_history:
            messages.extend(chat_history)

        # Add context from search
        messages.append({
            "role": "system",
            "content": f"Relevant context:\n{search_results}"
        })

        # Add current user question
        messages.append({
            "role": "user",
            "content": user_question
        })

        # Generate response using OpenAI
        response = self.openai_client.generate_response(messages)

        return response