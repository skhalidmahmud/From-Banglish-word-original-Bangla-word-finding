import csv
import os
import sys

# Force UTF-8 for the terminal so Bangla characters don't crash the script
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class BanglishConverter:
    def __init__(self, data_dir='./data'):
        self.data_dir = data_dir
        self.b2b_map = {}
        self.generator_map = {}
        self.word_lists = []
        self.load_data()

    def load_data(self):
        # 1. Load ben2bn.csv (The "known" mappings)
        b2b_path = os.path.join(self.data_dir, 'ben2bn.csv')
        if os.path.exists(b2b_path):
            with open(b2b_path, encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        self.b2b_map[row[0].lower()] = row[1]

        # 2. Load banGenerator.csv (The phoneme rules)
        gen_path = os.path.join(self.data_dir, 'banGenerator.csv')
        with open(gen_path, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                if not row or not row[0]: continue
                eng = row[0].lower()
                bangla_options = [x.strip() for x in row[1:] if x.strip() and x.strip() != '""']
                self.generator_map[eng] = bangla_options

        # 3. Load Word Lists (The "dictionaries")
        for list_name in ['BengaliWordList_40.txt', 'BengaliWordList_48.txt', 
                         'BengaliWordList_112.txt', 'BengaliWordList_439.txt']:
            path = os.path.join(self.data_dir, list_name)
            if os.path.exists(path):
                with open(path, encoding='utf-8-sig') as f:
                    # Using a set for lightning-fast lookups
                    self.word_lists.append(set(f.read().splitlines()))

    def split_banglish(self, word):
        """Splits banglish word into the longest possible phonemes found in map."""
        word = word.lower()
        parts = []
        i = 0
        # Sort keys by length so we find 'sh' before 's'
        sorted_keys = sorted(self.generator_map.keys(), key=len, reverse=True)
        
        while i < len(word):
            found = False
            for key in sorted_keys:
                if word.startswith(key, i):
                    parts.append(key)
                    i += len(key)
                    found = True
                    break
            if not found:
                # If we don't know the letter, just skip it
                i += 1
        return parts

    def is_valid_word(self, word):
        """Checks if the generated Bangla word exists in any of our dictionaries."""
        for w_list in self.word_lists:
            if word in w_list:
                return True
        return False

    def convert(self, banglish_word):
        banglish_word = banglish_word.lower()
        
        # Step 1: Check if we already know this exact word
        if banglish_word in self.b2b_map:
            return self.b2b_map[banglish_word]

        # Step 2: Split and Generate candidates
        phonemes = self.split_banglish(banglish_word)
        
        # Simple recursive generator to try combinations
        candidates = [""]
        for i, p in enumerate(phonemes):
            new_candidates = []
            options = self.generator_map.get(p, [])
            
            for cand in candidates:
                for opt in options:
                    new_candidates.append(cand + opt)
            candidates = new_candidates
            
            # To prevent memory explosion, we limit candidates
            if len(candidates) > 1000:
                candidates = candidates[:1000]

        # Step 3: Find the first candidate that is a real Bangla word
        for cand in candidates:
            if self.is_valid_word(cand):
                # Learning: Save it to our b2b map for next time!
                self.save_new_mapping(banglish_word, cand)
                return cand
        
        # If nothing found, return the first "best guess"
        return candidates[0] if candidates else "Not found"

    def save_new_mapping(self, eng, ban):
        b2b_path = os.path.join(self.data_dir, 'ben2bn.csv')
        self.b2b_map[eng] = ban
        with open(b2b_path, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([eng, ban])

# Testing the logic
if __name__ == "__main__":
    conv = BanglishConverter()
    test_word = input("Enter Banglish: ")
    print(f"Bangla Result: {conv.convert(test_word)}")
