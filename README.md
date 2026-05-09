# 🇧🇩 Banglish-to-Bangla: Phonetic Smart Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A rule-based and dictionary-validated NLP tool designed to convert Romanized Bengali (Banglish) into original Bangla script. This project leverages recursive phonetic mapping and automated dictionary validation to ensure high accuracy in transliteration.

## 🚀 Key Features
- **Smart Phonetic Splitting**: Intelligently breaks down Banglish words into phonetic components (e.g., `kh`, `sh`, `aa`).
- **Recursive Candidate Generation**: Explores multiple Bangla character possibilities for each English letter.
- **Dictionary Validation**: Validates generated candidates against a massive 400,000+ word Bengali dictionary.
- **Self-Learning Engine**: Automatically saves newly discovered mappings to a persistent database (`ben2bn.csv`).

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Data Formats**: CSV (Phonetic mappings), TXT (Dictionary word lists)
- **Algorithms**: Recursive Search, String Tokenization, Set-based Lookup

## 👥 The Team
This project was developed as part of the "Project Management" course by:
- **[Khalid Mahmud](https://github.com/skhalidmahmud)**
- **[Antora Ghosh](https://github.com/antoraghosh)**

---

## 📅 Development Roadmap

### ✅ Phase 1: Planning & Design
- Defined splitting rules for vowels and consonants.
- Designed the core data structure for phonetic mapping.

### ✅ Phase 2: Database Construction
- Compiled `banGenerator.csv` with multi-character mapping.
- Integrated 4 major Bengali word lists (40k, 48k, 112k, 439k words).

### ✅ Phase 3: Engine Development (Week 5)
- **Modularization**: Refactored notebook code into a robust `BanglishConverter` class.
- **Recursive Logic**: Implemented smart candidate generation to handle ambiguous vowels.
- **UTF-8 Support**: Fixed Windows terminal encoding issues for native script display.

### ⏳ Phase 4: Expansion (Coming Soon)
- [ ] Graphical User Interface (GUI) for desktop use.
- [ ] Support for complex conjuncts (যুক্তবর্ণ) improvement.
- [ ] Web-based API for integration into other apps.

---

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/skhalidmahmud/From-Banglish-word-original-Bangla-word-finding.git
cd From-Banglish-word-original-Bangla-word-finding
```

### 2. Run the Converter
```bash
python converter.py
```

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
