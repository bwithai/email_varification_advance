from fastapi import FastAPI, Depends, BackgroundTasks
from .config import Settings, get_env
from .database import get_db, Session
from . import schemas, crud, email, database

settings: Settings = get_env()
app = FastAPI(debug=settings.debug)
database.main()


@app.get('/')
def index():
    return {'message': 'Smart Slice notification service.'}


@app.post('/email')
def create_email_notification(email_notification: schemas.EmailNotification, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_email_notification = crud.create_notification(db, email_notification)
    background_tasks.add_task(email.send_email, db_email_notification, db)
    return {"id": db_email_notification.id, "subject": db_email_notification.subject}

