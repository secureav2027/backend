from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import auth, commands, health, protected

app = FastAPI(title="backend")

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(commands.router)

app.mount("/ui", StaticFiles(directory="static", html=True), name="ui")


@app.get("/")
def root():
    return {"status": "ok"}
