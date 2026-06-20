# Security

Responsible disclosure

If you discover a vulnerability, please report it privately by opening an
issue and prefixing it with `SECURITY:` and do not include exploit code in
the issue body. For critical vulnerabilities, contact the maintainer at
the email listed in the repository metadata.

Security tooling

- We recommend using `bandit` to scan for common security issues.
- Use `gitleaks` for secret scanning before pushing code.

No secrets

Do not commit secrets (API keys, tokens, private certificates). Use
`.env` files excluded from Git and populate using `.env.example`.
