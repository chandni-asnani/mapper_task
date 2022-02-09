from fastapi import FastAPI, Path
from pydantic import BaseModel
from fuzzywuzzy import fuzz
import psycopg2
import requests


def db_connect():
    ''' Database connection method '''
    conn = psycopg2.connect(
        database="mapper_task",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432",
    )
    return conn

app = FastAPI()

class Item(BaseModel):
    ''' Input Response '''
    make: str
    model_variant: str
    seating_capacity: int
    fuel: str



@app.post("/modellist/")
async def list_item(input_data:Item):
    ''' Api to get result '''
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT make, model || '_' || variant as model_variant FROM mappers where fuel='{input_data.fuel}' AND seatingcapacity={input_data.seating_capacity}")
    data = cur.fetchall()
    conn.commit()
    conn.close()
    if data:
        result = []
        for row in data:
            make = row[0]
            model_variant = row[1]
            make_match = fuzz.ratio(input_data.make, make)
            model_variant_match = fuzz.ratio(input_data.model_variant, model_variant)
            weighted_sum = (make_match + model_variant_match)/2
            # print(make, model_variant)
            # print(make_match, model_variant_match, weighted_sum)
            result.append(weighted_sum)
        res = data[result.index(max(result))]
        return {
            "score": max(result),
            "make": res[0],
            "model_variant": res[1],
            "fuel": input_data.fuel,
            "seatingCapacity": input_data.seating_capacity
        }
    else:
        return []