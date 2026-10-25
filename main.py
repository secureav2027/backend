from fastapi import FastAPI

from app.routers import health

app = FastAPI(title="backend")

app.include_router(health.router)


@app.get("/")
def root():
    return {"status": "ok"}
