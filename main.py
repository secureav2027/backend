from fastapi import FastAPI

from app.routers import auth, health, protected

app = FastAPI(title="backend")

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(protected.router)


@app.get("/")
def root():
    return {"status": "ok"}
