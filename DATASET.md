# Dataset Information: Banglish-to-Bangla

This project relies on several key datasets to perform accurate transliteration and word validation.

## 1. Phonetic Mapping (`banGenerator.csv`)
This is the core rulebook of the converter. It maps English character sequences to their corresponding Bangla characters.
- **EngLit**: The Romanized character or sequence (e.g., `a`, `aa`, `kh`).
- **Ben1 - Ben7**: Possible Bangla mappings in order of priority.

## 2. Bangla Word Lists (`bwl_*.txt`)
These files are used for dictionary validation. The system currently uses four lists:
- `BengaliWordList_40.txt`: Common words (40k).
- `BengaliWordList_48.txt`: Intermediate word list (48k).
- `BengaliWordList_112.txt`: Large word list (112k).
- `BengaliWordList_439.txt`: Comprehensive word list (439k).

## 3. Dynamic Cache (`ben2bn.csv`)
This file stores verified "Banglish -> Bangla" mappings. 
- It starts with a base set of common words.
- It grows automatically every time the `converter.py` finds a new valid word through generation.

## 4. Sources
The primary word lists were sourced and compiled from the [BengaliDictionary](https://github.com/MinhasKamal/BengaliDictionary) repository.
