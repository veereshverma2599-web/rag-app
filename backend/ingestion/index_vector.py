import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from ingestion.chunking import chunk
from app.core.paths import PDF_DIR, INDEX_PATH, META_PATH

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)

texts = []
meta = []

if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
    index = faiss.read_index(INDEX_PATH)
    texts, meta = pickle.load(open(META_PATH, "rb"))
else:
    index = None

all_chunks = []

for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        from pypdf import PdfReader
        reader = PdfReader(os.path.join(PDF_DIR, file))
        text = " ".join(p.extract_text() or "" for p in reader.pages)
        chunks = chunk(text)
        all_chunks.extend(chunks)
        meta.extend([file]*len(chunks))

if not all_chunks:
    print("No documents found.")
    exit()

embeddings = model.encode(all_chunks)

if index is None:
    index = faiss.IndexFlatL2(embeddings.shape[1])

index.add(embeddings)
texts.extend(all_chunks)

faiss.write_index(index, INDEX_PATH)
pickle.dump((texts, meta), open(META_PATH, "wb"))

print("Index updated successfully.")

