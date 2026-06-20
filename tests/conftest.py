import sys
from pathlib import Path


def pytest_configure(config):
    # Ensure repository root is on sys.path so in-repo imports like `utils` work
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))
