class CustomerAgent:

    def __init__(
        self,
        ai_service,
        db
    ):

        self.ai = ai_service

        self.db = db


    async def process_email(
        self,
        email_text: str
    ):

        # 1. AI understands email

        # 2. AI decides what to do

        # 3. Agent calls tool

        # 4. Tool returns data

        # 5. AI creates final response

        pass