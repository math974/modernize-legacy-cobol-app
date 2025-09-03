# PyPI Package Publication Setup

This document explains how to set up automatic publication to PyPI for this project.

## Prerequisites

1. **PyPI Account**: Create an account at [https://pypi.org](https://pypi.org)
2. **API Token**: Generate an API token in your PyPI account settings
3. **GitHub Secrets**: Add the API token to your GitHub repository secrets

## Setup Instructions

### 1. Create PyPI Account and API Token

1. Go to [https://pypi.org](https://pypi.org) and create an account
2. Go to Account Settings → API tokens
3. Create a new API token with scope "Entire account" or specific to your project
4. Copy the token (starts with `pypi-`)

### 2. Setup GitHub Environment and Secret

1. **Create Production Environment:**
   - Go to your GitHub repository
   - Navigate to Settings → Environments
   - Click "New environment"
   - Name: `prod`
   - Configure protection rules (optional but recommended):
     - Required reviewers
     - Wait timer
     - Deployment branches (only `main` or tags)

2. **Add Environment Secret:**
   - In the `prod` environment settings
   - Click "Add secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token (including the `pypi-` prefix)

### 3. Update Package Information

Before publishing, update these files with your information:

#### `setup.py` and `pyproject.toml`:
```python
author="Your Name"
author_email="your.email@example.com"
url="https://github.com/your-username/your-repo"
```

### 4. Create a Release

The package will be automatically published to PyPI when you create a tag starting with `v`:

```bash
# Create and push a tag
git tag v1.0.0
git push origin v1.0.0
```

Or create a release through GitHub's web interface.

## Package Installation

Once published, users can install your package with:

```bash
# Install the package
pip install legacy-cobol-modernization

# Install with development dependencies
pip install legacy-cobol-modernization[dev]

# Install with test dependencies only
pip install legacy-cobol-modernization[test]
```

## Usage After Installation

After installation, users can run the application using the console scripts:

```bash
# Run the accounting system
legacy-accounting

# Alternative command
cobol-accounting
```

## Package Structure

The package includes:

- **Main Application**: `main.py` - The Python accounting system
- **Test Files**: `test_*.py` - Unit and Golden Master tests
- **COBOL Sources**: `*.cob` - Original COBOL files for reference
- **Documentation**: `README.md`, `LICENSE`, etc.

## Local Testing

Before publishing, you can test the package locally:

```bash
# Build the package
python -m build

# Check the package
twine check dist/*

# Install locally for testing
pip install dist/legacy-cobol-modernization-1.0.0.tar.gz

# Test the console script
legacy-accounting
```

## Workflow Trigger

The PyPI publication workflow (`publish-pypi` job) runs when:

- A push event occurs
- The push is to a tag starting with `v` (e.g., `v1.0.0`, `v2.1.3`)
- All tests (compatibility, code quality, unit tests) pass
- The `production` environment is approved (if protection rules are enabled)

## Security Features

### Environment Protection

Using the `production` environment provides additional security:

- **Secret Isolation**: PyPI token is isolated to production deployments only
- **Review Requirements**: Optional manual approval before publishing
- **Branch Protection**: Can restrict deployments to specific branches/tags
- **Audit Trail**: All deployments are logged and tracked

### Recommended Protection Rules

1. **Required Reviewers**: Require manual approval before publishing
2. **Wait Timer**: Add a delay to prevent accidental immediate deployments
3. **Deployment Branches**: Restrict to tags matching `v*` pattern only

### Benefits

- **Prevents Accidental Publishing**: Manual review step catches mistakes
- **Secure Token Management**: API token only accessible in production context
- **Compliance**: Audit trail for all package publications
- **Team Safety**: Multiple eyes on production deployments

## Package Versioning

Update the version in both `setup.py` and `pyproject.toml` before creating a new release:

```python
version="1.0.1"  # Increment as needed
```

## Troubleshooting

### Common Issues:

1. **Authentication Error**: Check that `PYPI_API_TOKEN` secret is correctly set
2. **Package Name Conflict**: The package name might already exist on PyPI
3. **Version Conflict**: You cannot upload the same version twice
4. **Build Errors**: Ensure all dependencies are correctly specified

### Testing Publication:

For testing, you can use TestPyPI first:

1. Create account at [https://test.pypi.org](https://test.pypi.org)
2. Add `TEST_PYPI_API_TOKEN` secret
3. Modify the workflow to use TestPyPI URL temporarily
