from fastapi import FastAPI
import os
from src.routes.user_router import user_router
from src.routes.message_router import message_router
from src.utils.http_error_handler import HttpErrorHandler
from src.utils.config import Settings


settings = Settings()
print(settings.TWILIO_ACCOUNT_SID)


app = FastAPI()
app.title = "Encuestas Whastapp API"
app.version = "0.0.1"

app.add_middleware(HttpErrorHandler)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(message_router, prefix="/messages", tags=["Messages"])


@app.get("/")
def home():
    return f"[{os.getenv('TWILIO_AUTH_TOKEN')}]"
