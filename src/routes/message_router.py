from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from src.utils.twilio_client import TwilioClient
from src.models.send_survey_model import SendSurvey

message_router = APIRouter()


@message_router.post("/", status_code=status.HTTP_200_OK)
def send_message(body: SendSurvey):

    params = {
        "to": body.to_phone,
        "body": body.body if hasattr(body, "body") else None,
        "contentId": body.contentId if hasattr(body, "contentId") else None,
        "variables": body.variables if hasattr(body, "variables") else None,
    }

    params = {k: v for k, v in params.items() if v is not None}

    TwilioClient().send_message(**params)

    return JSONResponse(content="Message sent successfully.")
