import os
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/mapper_task', echo=False)

df = pd.read_excel("dataset.xlsx")
df = df.drop(["_id"], axis=1)
df.to_sql('mappers', con=engine, if_exists='append')