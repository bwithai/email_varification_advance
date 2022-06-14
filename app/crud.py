from sqlmodel import select
from .database import Session
from . import models, schemas


def get_notification_by_id(db: Session, notification_id: int):
    query = select(models.EmailNotification).where(models.EmailNotification.id == notification_id)
    return db.exec(query).first()


def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    query = select(models.EmailNotification).offset(skip).limit(limit)
    return db.exec(query).all()


def get_notification_by_email_to(db: Session, email: str):
    query = select(models.EmailNotification).where(models.EmailNotification.email_to == email.lower())
    return db.exec(query).first()


def get_notification_by_subject(db: Session, subject: str):
    query = select(models.EmailNotification).where(
        models.EmailNotification.subject.like("%{}%".format(subject.title())))
    return db.exec(query).first()


def get_notification_by_status(db: Session, status: bool):
    query = select(models.EmailNotification).where(models.EmailNotification.status == status)
    return db.exec(query).first()


def create_notification(db: Session, email_notification: schemas.EmailNotification):
    db_email_notification = models.EmailNotification(
        subject=email_notification.subject.title(),
        email_to=email_notification.email_to.lower(),
        email_body=email_notification.email_body,
    )
    db.add(db_email_notification)
    db.commit()
    db.refresh(db_email_notification)
    return db_email_notification


def update_notification(db: Session, db_email_notification, email_notification_data: schemas.UpdateEmailNotification):
    for key, value in email_notification_data.dict(exclude_unset=True).items():
        setattr(db_email_notification, key, value)
    db.add(db_email_notification)
    db.commit()
    db.refresh(db_email_notification)
    return db_email_notification
