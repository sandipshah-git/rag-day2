
# import pymupdf

# # Open PDF document
# doc = pymupdf.open("documents/python_notes.pdf")

# # Extract text from each page
# for page_number, page in enumerate(doc, start=1):

#     text = page.get_text()

#     print(f"\n--- Page {page_number} ---")

#     print(text)

# # Close document
# doc.close()


import pymupdf

doc = pymupdf.open("documents/python_notes.pdf")

with open("extracted_text.txt", "w", encoding="utf-8") as output:

    for page_number, page in enumerate(doc, start=1):

        text = page.get_text()

        output.write(f"\n--- Page {page_number} ---\n")
        output.write(text)

doc.close()

print("PDF extraction completed successfully!")
print("Check extracted_text.txt")
