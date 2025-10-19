from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Optional
import uvicorn
import os
from pathlib import Path

from parsers import parse_file
from chunker import chunk_text
from embed_store import EmbeddingStore
from llm_client import answer_with_gemini, answer_with_fallback

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
app = FastAPI(title="Multimodal Data Processing System")

emb_store = EmbeddingStore(index_path="faiss_index.idx", meta_path="faiss_meta.json")

@app.post("/upload/")
async def upload(files: List[UploadFile] = File(...)):
    saved = []
    for f in files:
        dest = DATA_DIR / f.filename
        with open(dest, "wb") as out:
            out.write(await f.read())
        saved.append(str(dest))
        parsed = parse_file(dest)
        for doc in parsed:
            chunks = chunk_text(doc["text"])
            for i, c in enumerate(chunks):
                meta = doc.get("meta", {}).copy()
                meta.update({"source": f.filename, "chunk_index": i})
                emb_store.add_document(c, meta)
    emb_store.save()
    return JSONResponse({"uploaded": saved})

@app.post("/query/")
async def query(q: str = Form(...), use_gemini: Optional[bool] = Form(True), k: int = Form(5)):
    hits = emb_store.search(q, top_k=k)
    context = "\n\n---\n\n".join([h["text"] for h in hits])
    if use_gemini:
        resp = answer_with_gemini(question=q, context=context, hits=hits)
    else:
        resp = answer_with_fallback(question=q, context=context, hits=hits)
    return {"answer": resp, "hits": hits}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
