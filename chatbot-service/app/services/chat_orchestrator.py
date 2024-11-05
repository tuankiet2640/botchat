from app.services.azure_openai import AzureOpenAIService
from app.services.azure_ai_search import AzureSearchService


class ChatOrchestrator:
    def __init__(
            self,
            openai_service: AzureOpenAIService,
            search_service: AzureSearchService
    ):
        self.openai_service = openai_service
        self.search_service = search_service

    async def process_message(
            self,
            message: str,
            conversation_id: str,
            user_id: str
    ) -> dict:
        # 1. Search relevant documents
        search_results = await self.search_service.search(message)

        # 2. Build context from search results
        context = self._build_context(search_results)

        # 3. Generate response using Azure OpenAI
        response = await self.openai_service.generate_response(
            message=message,
            context=context
        )

        return {
            "response": response,
            "sources": search_results
        }

    def _build_context(self, search_results: list) -> str:
        context = ""
        for result in search_results:
            context += f"{result}\n"
        return context