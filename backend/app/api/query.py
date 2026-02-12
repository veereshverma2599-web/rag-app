from fastapi import APIRouter
from app.services.retriever import retrieve
from app.services.context_builder import build_context
from app.services.llm import generate
from app.cache.redis_client import redis_client

router = APIRouter()

@router.get("/query")
async def query(q: str):

    cache_key = f"answer:{q}"
    cached = redis_client.get(cache_key)

    if cached:
        return {"answer": cached.decode(), "cached": True}

    chunks = retrieve(q)
    context = build_context(chunks)

    # await required because generate is async
    answer = await generate(q, context)

    # Redis expects string/bytes
    redis_client.setex(cache_key, 3600, answer)

    return {"answer": answer, "cached": False}
