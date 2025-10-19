import math
from typing import List

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100) -> List[str]:
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    chunks = []
    start = 0
    n = len(tokens)
    while start < n:
        end = min(start + chunk_size, n)
        chunk = " ".join(tokens[start:end])
        chunks.append(chunk)
        if end == n:
            break
        start = end - overlap
        if start < 0:
            start = 0
    return chunks