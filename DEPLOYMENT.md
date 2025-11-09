# Deployment Guide

## PyPI Publishing

Your project is now configured for automatic PyPI publishing via GitHub Actions.

### Automatic Publishing (Recommended)

1. **Create a GitHub Release**:
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Choose a tag (e.g., `v1.0.1`)
   - Write release notes
   - Click "Publish release"

2. **Automatic Build and Publish**:
   - The GitHub Actions workflow will automatically trigger
   - It will build the package and publish to PyPI
   - Check the Actions tab for progress

### Manual Publishing (Emergency)

If you need to publish manually:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (requires PYPI_API_TOKEN)
twine upload dist/*
```

## GitHub Pages Documentation

Documentation is automatically deployed when you push to `main` branch.

### Manual Deployment

```bash
# Install MkDocs
pip install mkdocs-material

# Build and deploy
mkdocs build
# The site/ directory contains the built documentation
```

## Pre-Deployment Checklist

- [ ] Version updated in `pyproject.toml`
- [ ] `CHANGELOG.md` updated with version notes
- [ ] All tests passing locally
- [ ] Documentation builds without errors
- [ ] Package builds successfully: `python -m build`
- [ ] Package passes checks: `python -m twine check dist/*`

## Environment Variables

The following secrets should be configured in GitHub repository settings:

- `PYPI_API_TOKEN`: Your PyPI API token for publishing

## URLs After Deployment

- **PyPI Package**: https://pypi.org/project/stackifier/
- **Documentation**: https://bryanthel.github.io/pip-stackifier
- **GitHub Repository**: https://github.com/BryanTheLai/pip-stackifier
