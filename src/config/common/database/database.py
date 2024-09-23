from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus
import pypyodbc as odbc

# Database connection details
SERVER_NAME = "185.4.176.50,5672"
DATABASE_NAME = "Res_Halditest_Db"
USER = "Haldi_test_Db"
PASSWORD = "osEx9H99V(/M"

# Construct connection string for pypyodbc
connection_string = f"""
    DRIVER={{SQL Server}}; 
    SERVER={SERVER_NAME}; 
    DATABASE={DATABASE_NAME}; 
    UID={USER}; 
    PWD={PASSWORD};
"""

# Establish the database connection using pypyodbc
try:
    conn = odbc.connect(connection_string)
    print("Database connection successful")
except Exception as e:
    print("Database connection failed")
    print(e)

# Create SQLAlchemy engine
engine = create_engine(f'mssql+pyodbc://', creator=lambda: conn, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = db_session.query_property()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example usage of SQLAlchemy engine
if __name__ == "__main__":
    # Perform database operations using engine
    with engine.connect() as connection:
        result = connection.execute("SELECT @@version;")
        print(result.scalar())  # Example query to test the connection


# from sqlalchemy import create_engine
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session
# from urllib.parse import quote_plus
# import pypyodbc as odbc

# # Database connection details
# # SERVER_NAME = "DESKTOP-RE9685A\\SQLEXPRESS"
# SERVER_NAME = "185.4.176.50,5672"
# # DATABASE_NAME = "Haldi"
# DATABASE_NAME="Res_Halditest_Db"

# # Construct connection string for pypyodbc
# connection_string = f"""
#     DRIVER={{SQL Server}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABASE_NAME};
# """

# # Establish the database connection using pypyodbc
# try:
#     conn = odbc.connect(connection_string)
#     print("Database connection successful")
# except Exception as e:
#     print("Database connection failed")
#     print(e)

# # Create SQLAlchemy engine
# engine = create_engine(f'mssql+pyodbc://', creator=lambda: conn, echo=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# Base = declarative_base()
# Base.query = db_session.query_property()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Example usage of SQLAlchemy engine
# if __name__ == "__main__":
#     # Perform database operations using engine
#     with engine.connect() as connection:
#         result = connection.execute("SELECT @@version;")
#         print(result.scalar())  # Example query to test the connection




# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session
# from urllib.parse import quote_plus

# # SQL Server connection string
# database_url = "mssql+pyodbc:///?odbc_connect={}".format(
#     quote_plus("Driver={ODBC Driver 17 for SQL Server};"
#                "Server=DESKTOP-QNP0IAE\\SQLEXPRESS;"
#                "Database=myNetworkDb;"
#                "Trusted_Connection=yes;")
# )

# # Alternative connection string with SQL Server Authentication
# # database_url = "mssql+pyodbc:///?odbc_connect={}".format(
# #     quote_plus("Driver={ODBC Driver 17 for SQL Server};"
# #                "Server=DESKTOP-QNP0IAE\\SQLEXPRESS;"
# #                "Database=myNetworkDb;"
# #                "UID=your_username;"
# #                "PWD=your_password;")
# # )

# engine = create_engine(database_url)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# Base = declarative_base()
# Base.query = db_session.query_property()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
