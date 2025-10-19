import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List, Dict
import os

class EmbeddingStore:
    def __init__(self, model_name="all-MiniLM-L6-v2", index_path="faiss_index.idx", meta_path="faiss_meta.json"):
        self.model = SentenceTransformer(model_name)
        self.index_path = index_path
        self.meta_path = meta_path
        self.dimension = self.model.get_sentence_embedding_dimension()
        self.index = None
        self.meta = [] 
        if os.path.exists(index_path) and os.path.exists(meta_path):
            self._load()
        else:
            self.index = faiss.IndexFlatIP(self.dimension) 

    def _load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.meta_path, "r", encoding="utf-8") as fh:
            self.meta = json.load(fh)

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "w", encoding="utf-8") as fh:
            json.dump(self.meta, fh, ensure_ascii=False, indent=2)

    def add_document(self, text: str, meta: Dict):
        vec = self.model.encode([text], convert_to_numpy=True)
        # normalize for IP
        faiss.normalize_L2(vec)
        self.index.add(vec)
        self.meta.append({"text": text, "meta": meta})

    def search(self, query: str, top_k: int = 5):
        qvec = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(qvec)
        D, I = self.index.search(qvec, top_k)
        hits = []
        for score, idx in zip(D[0], I[0]):
            if idx == -1 or idx >= len(self.meta):
                continue
            item = self.meta[idx]
            item_copy = item.copy()
            item_copy["score"] = float(score)
            hits.append(item_copy)
        return hits
