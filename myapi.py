from fastapi import FastAPI, Path
from pydantic import BaseModel

import uvicorn
import pickle

import pandas as pd

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)
app = FastAPI()


class itemInput(BaseModel):
    number : int


@app.get("/")
async def index():
    return {"Result": "Hellow World"}


@app.post("/prediction")
async def predict(item:itemInput):
    # df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    output = float(model.predict([item.number])[0][0])
    return {'predict':output}

if __name__ == '__main__':
    uvicorn.run("myapi:app", host='127.0.0.1')

