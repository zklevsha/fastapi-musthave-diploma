import os


def get_db_url() -> str:
    db_url = os.environ.get("DB_URL")
    if not db_url:
        raise ValueError('DB_URL enviroment variable is not set')
    return db_url
