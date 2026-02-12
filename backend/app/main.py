from fastapi import FastAPI
from app.api.query import router as query_router
from app.api.health import router as health_router
from app.services.retriever import load_index
app = FastAPI(title="RAG Backend")

app.include_router(query_router)
app.include_router(health_router)


@app.on_event("startup")
def startup():
    load_index()
    print("Index loaded if available.")
