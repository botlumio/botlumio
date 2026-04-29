# Contributing to Lumiobot

Thanks for your interest in improving Lumiobot! 🔆

This document explains how to contribute code, report issues, and propose
features.

## Code of Conduct

By participating, you agree to abide by our
[Code of Conduct](./CODE_OF_CONDUCT.md).

## Reporting Bugs

1. Check [existing issues](https://github.com/botlumio/botlumio/issues) first.
2. If none match, open a new issue and include:
   - What you expected to happen
   - What actually happened
   - Steps to reproduce
   - Environment (OS, Python version, etc.)
   - Screenshots or logs (redact secrets!)

For **security issues**, follow [SECURITY.md](./SECURITY.md) instead — do
**not** open a public issue.

## Suggesting Features

Open an issue with the `enhancement` label and describe:

- The problem the feature solves
- Your proposed solution
- Any alternatives you considered

## Development Workflow

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/botlumio.git
cd botlumio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy env template and fill in your keys
cp .env.example .env

# 4. Create a feature branch
git checkout -b feature/short-description

# 5. Make your changes, then commit
git commit -m "feat: short description of change"

# 6. Push and open a Pull Request
git push origin feature/short-description
```

## Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `refactor:` — code change that neither fixes a bug nor adds a feature
- `chore:` — tooling, dependencies, CI
- `security:` — security-related fix

## Pull Request Checklist

- [ ] Branch is up to date with `main`
- [ ] No secrets, API keys, or `.env` files committed
- [ ] Code is formatted and linted
- [ ] Existing tests still pass
- [ ] New behavior has tests where reasonable
- [ ] README / docs updated if user-visible behavior changed

## Style

- Python 3.11+
- Follow PEP 8
- Use type hints where reasonable
- Keep functions small and focused

## Questions?

Reach out on X: [@Zhenya718](https://x.com/Zhenya718) or via the bot at
[t.me/ailumio_bot](https://t.me/ailumio_bot).

🔆 Happy hacking!
