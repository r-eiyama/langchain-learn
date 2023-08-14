from typing import Optional

from fastapi import FastAPI
from routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


@app.get("/")
async def read_main():
    return {"msg": "Hello OpenAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


