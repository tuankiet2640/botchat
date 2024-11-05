# Azure AI Search Service
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

class AzureSearchService:
    def __init__(self, endpoint, index_name, api_key):
        self.endpoint = endpoint
        self.index_name = index_name
        self.api_key = api_key
        self.search_client = SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=AzureKeyCredential(self.api_key)
        )

    async def search(self, query: str, top: int = 3) -> list:
        search_results = self.search_client.search(
            search_text=query,
            select=["metadata_storage_name", "content"],
            top=top
        )
        sources = [result["metadata_storage_name"] for result in search_results]
        return sources