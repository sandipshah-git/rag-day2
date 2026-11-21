
import re
from pathlib import Path

# Step 1: Read extracted PDF text
input_file = Path("extracted_text.txt")
text = input_file.read_text(encoding="utf-8")

# Step 2: Remove extra spaces and tabs
text = re.sub(r"[ \t]+", " ", text)

# Step 3: Remove excessive blank lines
text = re.sub(r"\n{3,}", "\n\n", text)

# Step 4: Remove spaces at the beginning and end
text = text.strip()

# Step 5: Save cleaned text
output_file = Path("cleaned_text.txt")
output_file.write_text(text, encoding="utf-8")

print("Text cleaning completed!")
print(f"Cleaned text saved to: {output_file}")
