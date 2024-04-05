from fastapi import FastAPI

from .database import Base, engine
from .users.views import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(user_router)
