# Contributing to Stackifier

Thank you for your interest in contributing to Stackifier! This guide will help you get started.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BryanTheLai/pip-stackifier.git
   cd pip-stackifier
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install in development mode:**
   ```bash
   pip install -e ".[all,dev]"
   ```

## Development Workflow

### Running Tests

```bash
pytest tests/
pytest tests/ -v  # verbose output
pytest tests/test_trace.py  # specific test file
```

### Code Style

We follow standard Python conventions:
- Use type hints consistently
- Follow PEP 8 style guide
- Keep functions focused and simple
- Write docstrings for public APIs

### Before Submitting a PR

1. **Run tests:** Ensure all tests pass
2. **Update docs:** Add/update relevant documentation
3. **Add examples:** Include usage examples if adding new features
4. **Update CHANGELOG:** Add entry for your changes

## Contribution Guidelines

### Bug Reports

When reporting bugs, include:
- Python version
- Stackifier version
- Minimal reproducible example
- Expected vs actual behavior
- Error messages/stack traces

### Feature Requests

For new features, explain:
- Use case and motivation
- Proposed API/interface
- How it fits with existing functionality
- Whether you're willing to implement it

### Pull Requests

Good PRs:
- **Keep it simple:** Focus on one change at a time
- **Follow OpenAI schema:** Maintain compatibility with OpenAI chat format
- **Add tests:** Include tests for new functionality
- **Update README:** Add examples and API documentation
- **Small commits:** Make logical, atomic commits

## Project Principles

1. **Zero overhead by default:** No external dependencies required
2. **OpenAI compatible:** Follow OpenAI chat schema standards
3. **Drop-in integrations:** Minimal code changes to existing agents
4. **Production ready:** Proper error handling and resource cleanup
5. **Simple and focused:** Keep core focused on data collection

## Areas We Welcome Contributions

- New integration adapters (Anthropic, Cohere, etc.)
- Storage backends (PostgreSQL, MongoDB, etc.)
- Documentation improvements
- Bug fixes and performance optimizations
- Example applications

## Questions?

Feel free to open an issue for discussion before starting work on major features.

## Code of Conduct

Be respectful, constructive, and professional. We're all here to build something useful together.
