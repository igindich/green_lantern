import os
class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    PG_USER = "postgres"
    PG_PASSWORD = 'docker'
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "postgres"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
