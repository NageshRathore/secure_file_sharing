# app/init_db.py
from app.database import engine, Base
from app import models

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
