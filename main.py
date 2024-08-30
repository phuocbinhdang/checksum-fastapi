import uvicorn
from fastapi import FastAPI

from src.controllers import file

app = FastAPI()

app.include_router(file.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
