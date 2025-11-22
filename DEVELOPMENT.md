# Alsokkary Claude - Development Guide

## 📖 Project Structure
```
Alsokkary-claude/
├── main.py              # Main agent implementation
├── config.py            # Configuration settings
├── prompt_optimization.py # Prompt optimization module
├── test_main.py         # Unit tests
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── RESOURCES.md         # Important repositories and resources
├── CONTRIBUTING.md      # Contribution guidelines
├── LICENSE              # MIT License
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/mhdessouky-creator/Alsokkary-claude.git
cd Alsokkary-claude
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 5. Run the Agent
```bash
python main.py
```

## 🧪 Running Tests
```bash
pytest test_main.py -v
```

## 🎯 Using Prompt Optimization
```python
from prompt_optimization import PromptOptimizer

optimizer = PromptOptimizer()
optimized_prompt = optimizer.optimize("Your prompt here")
```

## 📚 Important Resources
See [RESOURCES.md](RESOURCES.md) for a complete list of important repositories and tools.

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Created:** 2025-11-22
**Maintained by:** mhdessouky-creator
