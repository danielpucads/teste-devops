
from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/helloword")
def read_root():
    return {"message": "Hello World"}



async def funcaoteste():
    return {"teste": True, "num_aleatorio":random.randint(0,1000) }