import PyPDF2
import argparse

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        original_text = ""
        for page_num in range(len(pdf_reader.pages)):
            original_text += pdf_reader.pages[page_num].extract_text()
    text = original_text.replace("\n", "")

    return text

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files.")
    parser.add_argument("pdf_path", type=str, help="Path of the PDF file to be extracted")
    args = parser.parse_args()

    extracted_text = extract_text_from_pdf(args.pdf_path)
    output_filename = args.pdf_path.rsplit('.', 1)[0] + ".txt"
    with open(output_filename, "w", encoding="utf-8") as txt_file:
        txt_file.write(extracted_text)
    
    print(f"Text saved in '{output_filename}'")

if __name__ == "__main__":
    main()