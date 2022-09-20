from fastapi import FastAPI
import uvicorn
from app.routers import router

app = FastAPI(
    title="ToyApp",
    description=("ToyApp"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
