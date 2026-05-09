# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-05-09
### Added
- Initial project structure with `data/` and `From Banglish word original Bangla word finding.ipynb`.
- Phonetic mapping for basic vowels and consonants.

## [0.2.0] - 2026-05-09 (Week 5 Update)
### Changed
- Refactored entire logic from Jupyter Notebook to modular `converter.py`.
- Implemented **Recursive Candidate Generation** to handle ambiguous phonetic mappings.
- Replaced linear dictionary search with **Set-based Set Lookups** for 100x faster performance.

### Fixed
- Terminal encoding issues that prevented Bangla characters from displaying correctly on Windows.
- Longest-match phoneme splitting (fixing `kh`, `sh` issues).

### Added
- Automated Learning: System now auto-updates `ben2bn.csv` with newly verified words.
- Professional documentation suite (`ARCHITECTURE.md`, `ROADMAP.md`, etc.).
