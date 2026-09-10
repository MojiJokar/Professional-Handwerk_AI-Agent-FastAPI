from openai import OpenAI
import os
from app.core.config import settings


class AIService:

    # def __init__(self):

    #     self.client = OpenAI(
    #         api_key=settings.openai_api_key
    #     )
    def __init__(self):
        api_key = os.getenv("NVIDIA_API_KEY")
        base_url = os.getenv("NVIDIA_BASE_URL")

        if not api_key:
            raise ValueError("NVIDIA_API_KEY is missing from .env")

        if not base_url:
            raise ValueError("NVIDIA_BASE_URL is missing from .env")

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    


    def analyze_email(
        self,
        email_text: str
    ):

        response = self.client.responses.create(

            model="gpt-5",

            input=[
                {
                    "role": "system",
                    "content": (
                        "You are a customer service "
                        "assistant for a German "
                        "heating company."
                    ),
                },
                {
                    "role": "user",
                    "content": email_text,
                },
            ],
        )

        return response.output_text