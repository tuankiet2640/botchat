# from openai import AsyncAzureOpenAI
# from app.config.settings import settings
#
#
# class AzureOpenAIService:
#     def __init__(self):
#         self.client = AsyncAzureOpenAI(
#             api_key=settings.AZURE_OPENAI_API_KEY,
#             api_version="2024-02-15-preview",
#             azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
#         )
#
#     async def generate_response(
#             self,
#             message: str,
#             context: str
#     ) -> str:
#         try:
#             completion = await self.client.chat.completions.create(
#                 model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
#                 messages=[
#                     {"role": "system", "content": context},
#                     {"role": "user", "content": message}
#                 ],
#                 temperature=settings.TEMPERATURE,
#                 max_tokens=settings.MAX_TOKENS,
#                 top_p=settings.TOP_P
#             )
#             return completion.choices[0].message.content
#         except Exception as e:
#             print(e)
#             raise
