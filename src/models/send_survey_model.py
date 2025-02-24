from pydantic import BaseModel


class SendSurvey(BaseModel):
    to_phone: str
    body: str | None = None
    contentId: str | None = None
    variables: dict[str, str] | None = None
