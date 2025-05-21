from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
DATABASE_URI = "mssql+pyodbc://sa:123@DESKTOP-BIONMCA/CricketCoach?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URI, echo=True)
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
Session = sessionmaker(bind=engine)

