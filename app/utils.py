from .config import Settings, get_env
from fastapi_mail import FastMail, ConnectionConfig
import urllib, os

settings: Settings = get_env()


def get_database_url():
    # url = "sqlite:///database.sqlite"
    url = "mysql+mysqldb://bwithai:sana123@localhost:3306/notifications"
    # URI = mysql+mysqldb: // syed: syedfurqan @ localhost:3306 / mobile_accessories
    # db_password = urllib.parse.quote_plus(settings.db_pass)
    # url = f"postgresql://{settings.db_user}:{db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    return url


def get_fastmail_connection_config():
    dir_path = os.path.dirname(__file__)
    template_path = os.path.join(dir_path, 'templates')
    fast_mail = FastMail(
        ConnectionConfig(
            MAIL_DEBUG=settings.mail_debug,
            MAIL_USERNAME=settings.mail_username,
            MAIL_PASSWORD=settings.mail_password,
            MAIL_FROM=settings.mail_from,
            MAIL_PORT=settings.mail_port,
            MAIL_SERVER=settings.mail_server,
            MAIL_FROM_NAME=settings.mail_from_name,
            MAIL_TLS=settings.mail_tls,
            MAIL_SSL=settings.mail_ssl,
            USE_CREDENTIALS=True,
            TEMPLATE_FOLDER=template_path
        )
    )
    return fast_mail
