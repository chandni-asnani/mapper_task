import os
from environs import Env
import pandas as pd
from sqlalchemy import create_engine
env = Env()
env.read_env()


engine = create_engine(f'postgresql://{env("DB_USER")}:{env("DB_PASSWORD")}@{env("DB_HOST")}:{env("DB_PORT")}/{env("DB_NAME")}', echo=False)

df = pd.read_excel("dataset.xlsx")
df = df.drop(["_id"], axis=1)
df.to_sql('mappers', con=engine, if_exists='append')
