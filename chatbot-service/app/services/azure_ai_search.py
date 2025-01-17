import os
import dotenv
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential

# Load environment variables
dotenv.load_dotenv()

# Azure AI Search configuration
AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_SERVICE")
AZURE_SEARCH_ENDPOINT = f"https://{AZURE_SEARCH_SERVICE}.search.windows.net"
AZURE_SEARCH_SERVICE_KEY = os.getenv("AZURE_SEARCH_SERVICE_KEY")
AZURE_SEARCH_FULL_INDEX = "gptkbindex"


class AzureAISearchClient:
    def __init__(self):
        search_service_cred = AzureKeyCredential(AZURE_SEARCH_SERVICE_KEY)
        self.search_client = SearchClient(
            AZURE_SEARCH_ENDPOINT,
            AZURE_SEARCH_FULL_INDEX,
            credential=search_service_cred
        )

    def search(self, user_question, embedding_func, top=5):
        """
        Perform semantic and vector search

        :param user_question: Query string
        :param embedding_func: Function to generate embeddings
        :param top: Number of top results to return
        :return: Formatted search results
        """
        user_question_vector = embedding_func(user_question)

        search_results = self.search_client.search(
            user_question,
            top=top,
            vector_queries=[
                VectorizedQuery(
                    vector=user_question_vector,
                    k_nearest_neighbors=50,
                    fields="embedding"
                )
            ],
            query_type="semantic",
            semantic_configuration_name="default-semantic-config"
        )

        sources = "\n".join([
            f"{doc['sourcefile']}: {doc['content']}\n" for doc in search_results
        ])

        return sources
