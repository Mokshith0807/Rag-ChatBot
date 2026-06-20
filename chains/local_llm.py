from llama_cpp import Llama


def load_local_llm():
    """
    Load the local GGUF model using llama.cpp.
    """

    llm = Llama(
        model_path="models/model.gguf",
        n_ctx=2048,
        n_threads=4,
        verbose=False,
    )

    return llm


def generate_local_answer(llm, prompt):
    """
    Generate a response from the local model.
    """

    output = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=128,
        temperature=0.1,
    )

    return output["choices"][0]["message"]["content"].strip()
