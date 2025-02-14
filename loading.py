import pandas as pd
from sqlalchemy import create_engine,text

cleaned_file = '/home/hadoop/DE2/transformed_data.csv'
df = pd.read_csv(cleaned_file)

username = "root"
password = "12345678"
host = "localhost"
port = "3306"
db_name = "diabetes_DB"
table_name = "diabetes"

def load_data():
    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}")

    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name};"))
        print(f"Database '{db_name}' created.")
    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}")

    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"{len(df)} new records loaded into '{table_name}' successfully.")
    except Exception as e:
        print(f"Error loading new data: {e}")
