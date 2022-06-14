from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class EmailNotification(BaseModel):
    id: Optional[int] = None
    subject: str
    email_to: str
    email_body: str
    status: bool = False

    class Config:
        orm_mode = True


class EmailNotificationInDB(EmailNotification):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UpdateEmailNotification(BaseModel):
    status: bool = False
    updated_at: datetime
