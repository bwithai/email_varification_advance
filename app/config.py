from pydantic import BaseSettings, EmailStr
from functools import lru_cache
from dotenv import load_dotenv


class Settings(BaseSettings):
    debug: bool = False
    db_host: str = ""
    db_name: str = ""
    db_user: str = ""
    db_pass: str = ""
    db_port: int = 5432
    mail_debug: bool = False
    mail_from: EmailStr = "user@domain.com"
    mail_from_name: str = ""
    mail_tls: bool = False
    mail_ssl: bool = False
    mail_server: str = ""
    mail_port: int = 25
    mail_username: EmailStr = "user@domain.com"
    mail_password: str = ""

    class Config:
        env_file = ".env.sample"


@lru_cache()
def get_env():
    load_dotenv()
    return Settings()
