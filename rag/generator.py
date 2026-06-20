"""Generator wrapper to produce answers from a local LLM chain.

This module exposes a small API for generating answers given a chain
or LLM-like object.
"""

from typing import List


def generate(llm_chain, docs: List[dict], query: str) -> str:
    """Generate an answer using the provided llm_chain.

    The function expects the llm_chain to be callable as
    `llm_chain.generate(context, query)` or have `__call__`.
    """
    # Try common call signatures for flexibility in testing
    context = "\n\n".join(
        getattr(d, "page_content", lambda: str(d))()
        if hasattr(d, "page_content")
        else d.get("content", "")
        for d in docs
    )
    if hasattr(llm_chain, "generate"):
        return llm_chain.generate(context=context, query=query)
    # fallback: call
    return llm_chain(context, query)
