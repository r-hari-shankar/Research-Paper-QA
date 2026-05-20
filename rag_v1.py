from pathlib import Path
importh chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import ollama

# ---------- 1. Load PDF ----------
def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

