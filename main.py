from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from database import Base, engine
from routers import auth, finance


Base.metadata.create_all(bind=engine)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/api/v1")
app.include_router(finance.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}