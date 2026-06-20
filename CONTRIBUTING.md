# Contributing

We welcome contributions. This document explains how to contribute in a
structured, predictable way so your work can be reviewed and merged
quickly.

1. Fork the repository and create a topic branch named `feature/xxx` or `fix/xxx`.
2. Run tests and linters locally before pushing changes.
3. Commit messages must be clear and follow the form:
   - `feat: short description` for features
   - `fix: short description` for bug fixes
   - `docs: short description` for documentation
   - `chore: short description` for maintenance
4. Open a Merge Request (MR) with a clear title and description explaining the change.
5. All MRs require at least one approving review and passing CI.

Git workflow

- Keep `main` protected. Work in branches off `main`.
- Rebase or merge `main` into your branch to resolve conflicts before MR.

Testing & Quality

- Run tests: `pytest -q`
- Run ruff: `ruff check .`
- Run bandit: `bandit -r . -ll`

Code of conduct

Be respectful and follow the repository CODE_OF_CONDUCT.md.
