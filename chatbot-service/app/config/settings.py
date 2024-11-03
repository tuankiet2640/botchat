from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "chatbot-service"
    APP_PORT: int = 8000
    INSTANCE_HOST: str = "localhost"
    INSTANCE_PORT: int = 8000

    # # Azure OpenAI Settings
    # AZURE_OPENAI_API_KEY: str
    # AZURE_OPENAI_ENDPOINT: str
    # AZURE_OPENAI_DEPLOYMENT_NAME: str
    #
    # # Azure AI Search Settings
    # AZURE_SEARCH_SERVICE_ENDPOINT: str
    # AZURE_SEARCH_INDEX_NAME: str
    # AZURE_SEARCH_API_KEY: str
    #
    # # Azure Document Intelligence Settings
    # AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT: str
    # AZURE_DOCUMENT_INTELLIGENCE_KEY: str
    #
    # # Application Settings
    # MAX_TOKENS: int = 2000
    # TEMPERATURE: float = 0.7
    # TOP_P: float = 0.95

    # Logging
    LOG_FILE_PATH: str = "D:\AI\logtest.txt"

    class Config:
        env_file = ".env"


settings = Settings()