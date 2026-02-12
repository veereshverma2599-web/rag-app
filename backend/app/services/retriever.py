import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer
from app.core.paths import INDEX_PATH, META_PATH

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

index = None
texts = []
meta = []

def load_index():
    global index, texts, meta

    if index is not None:
        return

    if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
        index = faiss.read_index(INDEX_PATH)
        texts, meta = pickle.load(open(META_PATH, "rb"))
    else:
        index = None
        texts = []
        meta = []

def retrieve(query: str, topk: int = 5):
    load_index()

    if index is None:
        return []

    qv = model.encode([query])
    _, I = index.search(qv, topk)
    return [texts[i] for i in I[0]]

