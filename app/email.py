from datetime import datetime
from fastapi_mail import MessageSchema
from .database import Session
from . import utils, schemas, crud

fast_mail = utils.get_fastmail_connection_config()


async def  send_email(email_notification: schemas.EmailNotificationInDB, db: Session):
    email = MessageSchema(
        subject=email_notification.subject,
        recipients=[email_notification.email_to],
        body=email_notification.email_body,
        subtype='html',
    )

    await fast_mail.send_message(email, template_name='email.html')
    update_email_notification = schemas.UpdateEmailNotification(
        status=True,
        updated_at=datetime.now()
    )
    crud.update_notification(db, email_notification, update_email_notification)

