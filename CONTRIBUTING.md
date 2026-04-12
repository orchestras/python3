# Contributing

Thank you for contributing to this project! Please read this guide before opening issues or PRs.

## Prerequisites

- [Mise](https://mise.jdx.dev) — tool version manager
- [UV](https://docs.astral.sh/uv/) — Python package manager (managed by mise)
- [Git](https://git-scm.com) with GPG signing configured (optional but recommended)
- [gh CLI](https://cli.github.com) — for `mise run vcs:protect` and scanning tasks

## Setup

```bash
# Clone the repo
git clone https://github.com/orchestras/python3
cd python3

# Initialise everything
mise run project:init
```

This will:
1. Install Python, UV, Ruff, and delta via mise
2. Install Python dependencies with `uv sync`
3. Configure local git settings (delta pager, rebase-only, hooks path)
4. Sync tags from remote
5. Install shell completions

## Development Workflow

### Branch naming

```
feat/<description>
fix/<description>
chore/<description>
refactor/<description>
```

### Making changes

```bash
# Create a feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feat/my-feature

# Make your changes...
mise run ci:all   # full pipeline (must pass before committing)

# Commit with Conventional Commits format
git add .
git commit -m "feat: add my new feature"

# Keep up to date with develop (rebase, never merge)
mise run vcs:rebase

# Push
git push -u origin feat/my-feature
```

### Opening a PR

- Target `develop` (not `main`)
- Fill out the PR template completely
- All required status checks must pass: `lint`, `typecheck`, `test`, `security`
- At least 1 approving review required

## Code Standards

### Style

All code is formatted and linted by Ruff. Run:

```bash
mise run fmt       # format
mise run lint      # lint
mise run lint:fix  # auto-fix lint issues
```

### Type annotations

All public functions must have complete type annotations. Run:

```bash
mise run typecheck   # ty check
```

### Tests

All new features must include tests. Tests live in `tests/` and follow the `test_*.py` naming convention.

```bash
mise run test        # run tests
mise run test:cov    # with coverage (must stay above 80%)
```

### Docstrings

Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for all public functions and classes.

```python
def my_function(arg: str) -> int:
    """Brief one-line description.

    Args:
        arg: Description of the argument.

    Returns:
        Description of return value.

    Raises:
        ValueError: When the input is invalid.
    """
```

### Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new feature
fix: fix a bug
docs: update documentation
chore: maintenance task
refactor: code restructuring without behaviour change
test: add or fix tests
ci: changes to CI configuration
```

The `commit-msg` hook enforces this format.

## Releasing

Releases are managed by the maintainers:

1. Changes accumulate on `develop`
2. When ready: `mise run vcs:release` (rebases develop into main)
3. On main: `mise run bump:patch/minor/major` → commits version bump + creates tag
4. `mise run tag:push` → triggers the release workflow
5. CI builds PyInstaller binaries for all platforms and creates a GitHub Release

## Security

- Never commit secrets, credentials, or API keys
- Use `mise run scan:secrets` before pushing
- Use `mise run scan:deps` to audit dependencies
- Report security vulnerabilities privately via GitHub Security Advisories
