
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}