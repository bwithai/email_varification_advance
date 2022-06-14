from sqlmodel import SQLModel, create_engine, Session
from . import utils


# Create DB Engine and Session
engine = create_engine(utils.get_database_url(), echo=True)
SessionLocal = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()


# Dependency
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    main()
