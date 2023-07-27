import psycopg2
from config import config
from get_hh_api import hh_api

PARAMS = config("config.ini", "postgresql")

data = hh_api()


# Значения для таблицы jobs и company


def create_database(params: dict):
    """Функция для создания таблиц"""
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS vacancy(
                vacancy_id int,
                vacancy_name varchar(50) NOT NULL,
                published_date date,
                salary_from int,
                salary_to int,
                url varchar(50),
                requirement text
                )
            """)
    conn.commit()