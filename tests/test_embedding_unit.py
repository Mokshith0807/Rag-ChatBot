from embeddings.embedder import load_embedding_model


def test_embedding_model():
    model = load_embedding_model()
    vec = model.encode("Hello")
    assert len(vec) == 384
