import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")
PDF_DIR = os.path.join(BASE_DIR, "ingestion", "pdfs")

INDEX_PATH = os.path.join(DATA_DIR, "vector.index")
META_PATH = os.path.join(DATA_DIR, "meta.pkl")
