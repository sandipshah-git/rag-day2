
import pymupdf
import re
import json
from pathlib import Path

# Step 1: Open the PDF
pdf_path = Path("documents/python_notes.pdf")
doc = pymupdf.open(pdf_path)

documents = []

# Step 2: Extract each page
for page_number, page in enumerate(doc, start=1):

    text = page.get_text()

    # Step 3: Clean the text
    
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    
    # Remove excessive spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)
    
    # Reduce 3 or more newline sequences to 2
    text = re.sub(r"(\n[ \t]*){3,}", "\n\n", text)
    
    # Remove unnecessary whitespace at the beginning and end
    text = text.strip()


    # Step 4: Attach metadata
    document = {
        "text": text,
        "metadata": {
            "source": pdf_path.name,
            "page": page_number
        }
    }

    documents.append(document)

# Step 5: Close PDF
doc.close()

# Step 6: Save structured data
output_path = Path("documents.json")

output_path.write_text(
    json.dumps(documents, indent=4, ensure_ascii=False),
    encoding="utf-8"
)

print("PDF metadata extraction completed!")
print(f"Total pages processed: {len(documents)}")
print(f"Saved to: {output_path}")
