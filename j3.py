import json
from collections import Counter

def is_english(text):
    try:
        text.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False
# Load input JSON
with open("flowers_processed.json", "r") as f:
    data = json.load(f)

# Extract only English species names
species_list = [entry["species"] for entry in data if is_english(entry["species"])]

# Count repetitions
species_count = Counter(species_list)

# Save result
with open("species.json", "w") as f:
    json.dump(species_count, f, indent=4, ensure_ascii=False)

print("Species counts saved to species_counts.json (non-English ignored)")
