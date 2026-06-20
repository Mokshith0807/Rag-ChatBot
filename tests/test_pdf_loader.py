from utils.pdf_loader import load_pdf


def test_pdf_loader():
    docs = load_pdf("data/raw/Unit 1_SCM.pdf")
    assert len(docs) > 0
