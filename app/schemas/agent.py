from pydantic import BaseModel


class EmailRequest(BaseModel):

    email_text: str


class AgentResponse(BaseModel):

    action: str

    customer_id: int | None

    response: str