import re
from pypdf import PdfReader

reader = PdfReader("./test-assets/2-1.pdf")
search_number = "20275"

found = False

for page_index, page in enumerate(reader.pages):
    text = page.extract_text()
    if not text:
        continue

    if search_number in text:
        found = True
        print(f"\nFound on page {page_index + 1}")

        i = text.find(search_number)

        line_start = text.rfind('\n', 0, i) + 1
        line_end = text.find('\n', i)
        if line_end == -1:
            line_end = len(text)

        line = text[line_start:line_end]
        print("Line:", line)

        # Remove seat number
        clean_line = line.replace(search_number, "", 1)

        # Look for 6-digit mark
        match = re.search(r'\d{6}', clean_line)

        if match:
            mark = match.group()
            exam = int(mark[0:2])
            labs = int(mark[2:4])
            total = int(mark[4:6])

            print("Exam:", exam)
            print("Labs:", labs)
            print("Total:", total)
        else:
            print("Mark: Not available or blocked")

        break

if not found:
    print("Seat number not found in PDF.")