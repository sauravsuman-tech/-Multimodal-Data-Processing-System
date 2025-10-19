from typing import List, Dict
import os


def answer_with_gemini(question: str, context: str, hits: List[Dict]) -> str:
    """
    Replace this function with an actual call to Gemini Free API SDK or HTTP endpoint.
    Provide `context` (retrieved chunks) to the model and ask it to answer the question.
    """
    # ---------------------------------------------------------------------------------
    # PSEUDO: build a prompt for the model:
    prompt = f"""You are given extracted context documents and a user question. Use only the context to answer concisely.
Context:
{context}

Question: {question}

Answer (cite source chunk_index and source if needed):"""
    # ---------------------------------------------------------------------------------
    # TODO: call Gemini API here, e.g. requests.post(...) or the Google Cloud client.
    # For now we return a placeholder.
    return "(gemini stub) Replace this with a real Gemini API call.\n\n" + prompt[:1000]


def answer_with_fallback(question: str, context: str, hits: List[Dict]) -> str:
    """
    A simple non-LLM heuristic: return the top hit text and the sources.
    This is for cases where you truly don't want to call an LLM.
    """
    answer_lines = []
    for h in hits:
        s = h.get("meta", {})
        source = s.get("source", "unknown")
        ci = s.get("chunk_index", -1)
        answer_lines.append(f"[{source} - chunk {ci}] {h['text'][:400]}...")
    if not answer_lines:
        return "No relevant context found."
    return "Top matches:\n\n" + "\n\n---\n\n".join(answer_lines)
