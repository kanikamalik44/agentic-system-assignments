from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/search")
def search(
    name: Optional[str] = Query(None),
    age: Optional[int] = Query(None)
):
    return {
        "name": name,
        "age": age
    }