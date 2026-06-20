# User Manual

This manual helps users run and interact with the Streamlit RAG Chatbot.

1. Setup

- Ensure Python 3.10+ is installed.
- Create a virtual environment and install requirements: `pip install -r requirements.txt`.
- Copy `.env.example` to `.env` and edit values as needed.

2. Run

- Start the app: `streamlit run app.py`
- The UI runs on `http://localhost:8501` by default.

3. Upload and Query

- Upload a PDF using the file uploader.
- The system will process and index the document.
- Enter a question and press `Get Answer`.

4. Files and Storage

- Raw uploads are stored in `data/raw/` (ignored by git).
- FAISS indexes are stored in `vectorstore/faiss_index/`.

5. Troubleshooting

- If embeddings fail, ensure required model files are in `models/` and `requirements.txt` satisfied.
- Increase Streamlit log level or consult `logs/` for debug output.
