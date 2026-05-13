# 🇧🇩 Banglish-to-Bangla: Phonetic Smart Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A rule-based and dictionary-validated NLP tool designed to convert Romanized Bengali (Banglish) into original Bangla script. This project leverages recursive phonetic mapping and automated dictionary validation to ensure high accuracy in transliteration.

## 🚀 Key Features
- **Modern Web UI**: A stunning glassmorphic interface for real-time conversion.
- **FastAPI Backend**: High-performance API for integration into other apps.
- **Smart Phonetic Splitting**: Intelligently breaks down Banglish words into phonetic components.
- **Recursive Candidate Generation**: Explores multiple Bangla character possibilities.
- **Dictionary Validation**: Validates generated candidates against 400,000+ words.
- **Self-Learning Engine**: Automatically saves newly discovered mappings.

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/skhalidmahmud/From-Banglish-word-original-Bangla-word-finding.git
cd From-Banglish-word-original-Bangla-word-finding
```

### 2. Start the Web App (Recommended)
This will install dependencies and start the local server.
```bash
python run.py
```
Then open your browser at **http://localhost:8000**.

### 3. CLI Mode
For a simple terminal-based experience:
```bash
python converter.py
```

## 🛠️ API Documentation
The backend is powered by FastAPI. Once running, you can access:
- **Interactive Docs**: `http://localhost:8000/docs`
- **Conversion Endpoint**: `POST /convert` with body `{"text": "your banglish text"}`

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
