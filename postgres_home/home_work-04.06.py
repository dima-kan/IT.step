import dotenv
import os
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DB")

db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"


engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()


def show_groups(session):
    query = """
    SELECT *
    FROM GROUPS
    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

# show_groups(session)

# вивести інформацію про всіх викладачів


def show_teacher(session):
    query = """
    SELECT *
    FROM TEACHERS
    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

# show_teacher(session)


# ▷ вивести назви усіх кафедр


def show_department(session):
    query = """
    SELECT *
    FROM DEPARTMENTS
    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

# show_department(session)

def get_teachers_group(session):
    query = """
    SELECT T.NAME, T.SURNAME
    FROM TEACHERS T
    JOIN LECTURES L ON L.TEACHERID = T.ID
    JOIN GROUPSLECTURES GL ON GL.LECTUREID = L.ID
    JOIN GROUPS G ON G.ID = GL.GROUPID
    WHERE G.NAME = 'PI-21'
    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

# get_teachers_group(session)

# вивести назви кафедр і груп, які до них відносяться,

def get_departments_groups(session):
    query = """
    SELECT D.NAME, G.NAME
    FROM DEPARTMENTS D
    JOIN GROUPS G ON G.DEPARTMENTID = D.ID;
    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

get_departments_groups(session)