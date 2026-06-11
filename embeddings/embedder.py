from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL


def load_embedding_model():

    model = SentenceTransformer(
        EMBEDDING_MODEL
    )

    return model
