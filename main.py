
from fastapi import FastAPI

app = FastAPI()


@app.get("/helloword")
def read_root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}