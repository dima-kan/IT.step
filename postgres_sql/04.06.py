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

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))

# query = """
#     SELECT *
#     FROM
# """
# query = text(query)
#
#
# result = session.execute(query)
#
# for row in result:
#     print(row)



# ▷ Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які не перебувають у відпустці;
# ▷ Вивести назви палат, які знаходяться у певному відділенні;
# Практичне завдання
# 1
# ▷ Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;
# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.

# Вивести прізвища лікарів та їх спеціалізації;
def show_doctors(session):
    query = """
        SELECT D.SURNAME,S.NAME
        FROM doctorsspecializations DS
        JOIN DOCTORS D ON DS.doctor_id = D.id
        JOIN specializations S ON DS.specialization_id = S.ID

    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


# show_doctors(session)



# ▷ Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які перебувають у відпустці;

def show_doctors_salary(session):
    query = """
        SELECT D.SURNAME,D.SALARY + D.PREMIUM
        FROM DOCTORS D
        JOIN VACATIONS V ON D.ID = V.DOCTOR_ID
        WHERE V.ENDDATE > CURRENT_DATE AND V.STARTDATE < CURRENT_DATE


    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)

# show_doctors_salary(session)

# Вивести назви палат, які знаходяться у певному відділенні;



def _show_name_departments(session):
    query = """
    SELECT NAME
    FROM DEPARTMENTS

    """
    query = text(query)
    result = session.execute(query)
    for row in result:
        print(row)

def show_wards(session):
    _show_name_departments(session)
    dep_name = input("Введіть назву відділення")

    query = f"""
    SELECT *
    FROM WARDS W
        JOIN DEPARTMENTS D ON D.ID = W.DEPARTMENT_ID
    WHERE D.NAME = '{dep_name}'
    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


# show_wards(session)



# Вивести усі пожертвування за вказаний місяць у
# # вигляді: відділення, спонсор, сума пожертвування, дата
# # пожертвування;


def show_donation(session):
    month_number = input("Введіть місяць число ")
    year_number = input("Введіть рік ")
    query = f"""
        SELECT DEP.NAME, S.NAME, D.AMOUNT, D.DONATION_DATE
        FROM DONATIONS D
            JOIN DEPARTMENTS DEP ON D.DEPARTMENT_ID = DEP.ID
            JOIN SPONSORS S ON D.SPONSOR_ID = S.ID
        WHERE  EXTRACT(MONTH FROM DONATION_DATE) = '{month_number}'
            AND EXTRACT(YEAR FROM DONATION_DATE) = '{year_number}'

    """
    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


# show_donation(session)