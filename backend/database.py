from django.conf import settings
from sqlalchemy import URL, create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = URL.create(
    drivername="sqlite",
    database=str(settings.DATABASES["default"]["NAME"]),
)

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},
)

@event.listens_for(engine, "connect")
def enable_foreign_keys(connection, connection_record):
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass