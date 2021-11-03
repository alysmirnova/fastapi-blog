from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings


engine = create_engine(
    settings.database_url
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
