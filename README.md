# RAG Chatbot - Production-Grade Open Source Project

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%20v3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Code Quality](https://img.shields.io/badge/code--quality-high-brightgreen)]()

An advanced Retrieval-Augmented Generation (RAG) chatbot that combines local document processing with large language models. Built with Streamlit, LangChain, FAISS, and llama.cpp for fully offline, privacy-preserving AI interactions.

## 🚀 Features

- **📄 PDF Processing**: Upload and process PDF documents with intelligent chunking
- **🔍 Semantic Search**: Vector-based retrieval using FAISS for fast similarity search
- **🤖 Local LLM Integration**: Run open-source models locally with llama.cpp (fully offline)
- **🧠 Advanced RAG Pipeline**: Context-aware generation with source attribution
- **💻 Web UI**: Interactive Streamlit interface for document upload and querying
- **🔐 Privacy-First**: No cloud dependencies, all processing remains local
- **⚡ High Performance**: Optimized chunking, embedding, and retrieval strategies
- **📦 Containerized**: Docker support for easy deployment

## 🏗️ Architecture

The project implements a multi-stage RAG (Retrieval-Augmented Generation) pipeline:

```
User Input (Question)
        ↓
    [Query Encoder]
        ↓
   [FAISS Vector DB]
        ↓
  [Semantic Retrieval] → Top-K Relevant Documents
        ↓
  [Context Builder]
        ↓
   [Local LLM Chain]
        ↓
   [Structured Answer + Sources]
```

**Components:**
- **Retriever** (`embeddings/embedder.py`): Converts queries into dense vectors
- **Vector Store** (`vectorstore/faiss_store.py`): Efficient similarity search
- **Generator** (`chains/rag_chain.py`): Local LLM-powered answer generation
- **Processor** (`utils/pdf_processor.py`): Document chunking and indexing

For detailed architecture documentation, see [AGENTS.md](AGENTS.md).

## 📋 Requirements

- Python 3.10 or higher
- 8GB+ RAM (recommended for smooth operation)
- 2GB+ disk space for models and indexes
- GPU support (optional, for faster inference)

## 🔧 Installation

### Quick Start (Linux/macOS)

```bash
# Clone the repository
git clone <repository-url>
cd rag-chatbot

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Run the Streamlit app
streamlit run app.py
```

### Docker Setup

```bash
# Build the Docker image
docker build -t rag-chatbot:latest .

# Run the container
docker run -p 8501:8501 rag-chatbot:latest
```

Visit `http://localhost:8501` in your browser.

## 📖 Usage Guide

### Basic Workflow

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```
   Opens in your browser at `http://localhost:8501`

2. **Upload a PDF Document**
   - Click "Upload a PDF" and select a document
   - The system processes the PDF and creates embeddings automatically
   - Status updates show processing progress

3. **Ask Questions**
   - Enter your question in the text field
   - Click "Get Answer" to receive a response with source attribution

### Advanced Usage

See [USER_MANUAL.md](USER_MANUAL.md) for detailed setup instructions, troubleshooting, and advanced configuration options.

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/test_retriever.py -v

# Run with coverage
pytest --cov=. tests/
```

## 🔒 Security

This project follows security best practices:

- Local-only processing (no external API calls)
- No user data storage or tracking
- Regular dependency updates
- Vulnerability scanning with bandit

For security issues, please refer to [SECURITY.md](SECURITY.md).

## 🚦 Quality Assurance

The project uses multiple code quality tools:

- **Ruff**: Fast Python linter
- **Black/Ruff Format**: Code formatting
- **MyPy**: Static type checking
- **Bandit**: Security scanning
- **Pre-commit Hooks**: Automated checks before commits

Run code quality checks:

```bash
# Run all quality checks
ruff check .
ruff format . --check
mypy .
bandit -r . -ll
```

## 🤝 Contributing

We welcome contributions! Please review our contribution guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

**Quick Guide:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and test thoroughly
4. Commit with clear messages (`git commit -m "Add amazing feature"`)
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📚 Documentation

- **[README.md](README.md)** - Project overview and quick start
- **[USER_MANUAL.md](USER_MANUAL.md)** - Comprehensive usage guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[AGENTS.md](AGENTS.md)** - RAG architecture and agent design
- **[SECURITY.md](SECURITY.md)** - Security policies and reporting
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community standards

## 🎯 Roadmap

### v1.0 (Current)
- ✅ Basic RAG pipeline with FAISS
- ✅ Streamlit web interface
- ✅ Local LLM support (llama.cpp)
- ✅ PDF processing with intelligent chunking

### v1.1 (Planned)
- [ ] Multi-format document support (DOCX, TXT, Markdown)
- [ ] Conversation history and context management
- [ ] Fine-tuning capabilities
- [ ] Performance optimization and caching

### v1.2+ (Future)
- [ ] Web API with FastAPI
- [ ] Kubernetes deployment templates
- [ ] Advanced query expansion techniques
- [ ] Multi-language support

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0** (AGPLv3). See [LICENSE](LICENSE) file for full details.

**Key Points:**
- Commercial use is allowed
- Source code distribution is required if you modify the project
- Same license must apply to modifications
- Network use triggers copyleft provisions

## 👥 Authors & Contributors

- **Mokshith** - Original Author and Maintainer

## 🆘 Support & Issues

- **Issues**: Report bugs and feature requests on [GitLab Issues](https://code.swecha.org/internship/2026/gitam/agent-skills/-/issues)
- **Discussions**: Join community discussions
- **Documentation**: Check [USER_MANUAL.md](USER_MANUAL.md) for FAQs

## 🙏 Acknowledgments

- LangChain team for the excellent RAG framework
- FAISS team for vector search optimization
- Streamlit team for the intuitive web framework
- Open source community for invaluable tools

## 📞 Contact

For questions or feedback:
- Open an issue on the repository
- Send a pull request with improvements
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

---

**Made with ❤️ for the open-source community**

Built as part of SWECHA Internship Program - GITAM 2026
