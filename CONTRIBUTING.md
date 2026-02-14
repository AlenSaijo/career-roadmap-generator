# Contributing to Career Roadmap Generator

Thank you for your interest in contributing! Here's how you can help.

## Getting Started

### Prerequisites
- Python 3.9+
- Git
- pip or conda

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/career-roadmap-generator.git
cd career-roadmap-generator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` to test your changes.

## Making Changes

### Branch Naming
- Feature: `feature/feature-name`
- Bug fix: `bugfix/bug-description`
- Documentation: `docs/doc-name`

Example:
```bash
git checkout -b feature/add-new-skill-category
```

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable/function names
- Add comments for complex logic
- Keep functions focused and small

### Commit Messages
Use clear, concise commit messages:

```
✨ Add new feature description
🐛 Fix bug with specific issue
📝 Update documentation
🎨 Improve UI/styling
```

### Testing
Test your changes thoroughly:
- Test all API endpoints manually
- Test frontend UI changes
- Check PDF upload functionality
- Verify game mechanics

## Areas for Contribution

### High Priority
- [ ] Add user authentication
- [ ] Connect to database (SQLite/PostgreSQL)
- [ ] Email notifications for progress
- [ ] User profile/dashboard
- [ ] Save/load roadmaps
- [ ] Dark/light theme toggle

### Medium Priority
- [ ] Add more interview questions
- [ ] Enhanced skill database
- [ ] Better PDF parsing
- [ ] Progress tracking
- [ ] Export roadmaps to PDF
- [ ] Additional games/features

### Low Priority
- [ ] UI/UX improvements
- [ ] Additional documentation
- [ ] Code refactoring
- [ ] Performance optimization
- [ ] Mobile app (React Native/Flutter)

## Pull Request Process

1. **Fork the repository** on GitHub
2. **Create a feature branch** with a descriptive name
3. **Make your changes** and test thoroughly
4. **Commit with clear messages** following conventions
5. **Push to your fork**
6. **Create a Pull Request** with:
   - Clear title and description
   - Reference any related issues (#123)
   - Screenshots for UI changes
   - List of changes made

### PR Guidelines
- Keep PRs focused on one feature/fix
- Update documentation if needed
- Add tests if applicable
- Follow the code style
- Be open to feedback

## Reporting Issues

### Bug Reports
Include:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages/screenshots

### Feature Requests
Include:
- Clear use case
- Why it's useful
- Suggested implementation (optional)
- Examples

## Code Review Process

1. At least one maintainer will review
2. Changes may be requested
3. Once approved, the PR will be merged
4. Your contribution will be credited!

## Community Guidelines

- Be respectful and inclusive
- Discuss ideas constructively
- Help others learn
- Share knowledge
- Celebrate contributions

## Questions?

- Open an issue with questions tag
- Check existing documentation
- Review previous issues/PRs
- Ask in pull request comments

## Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Credited in releases
- Mentioned in PRs

Thank you for contributing! 🎉
