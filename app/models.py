from typing import Optional
from sqlmodel import Field, SQLModel, Column, TEXT
from datetime import datetime


class EmailNotification(SQLModel, table=True):
    __tablename__ = "email_notifications"
    id: Optional[int] = Field(default=None, primary_key=True)
    subject: str
    email_to: str
    email_body: str = Field(sa_column=Column(TEXT))
    status: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
