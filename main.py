from pypdf import PdfReader
reader = PdfReader("./test-assets/2-1.pdf")
number_of_pages = len(reader.pages)
pages = reader.pages[0:number_of_pages]
# text = page.extract_text()
for page in pages:
    print(page.extract_text())