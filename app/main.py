from fastapi import FastAPI

app=FastAPI()

@app("/")
def read_root():
    return {"Hello":"world"}

@app("/items/{item_id}")
def read_item(item_id: int | None=None):
    return {"item_id":item_id}