import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        original_text = ""
        for page_num in range(len(pdf_reader.pages)):
            original_text += pdf_reader.pages[page_num].extract_text()
    text = original_text.replace("\n", "")

    return text

def main():
    for filename in os.listdir('pdf'):
        os.chdir('pdf')
        if ' ' in filename:
            os.rename(filename, filename.replace(' ', '_'))
            filename = filename.replace(' ', '_')
            print('change filename... padding done!')
        extracted_text = extract_text_from_pdf(filename)
        output_filename = filename.rsplit('.', 1)[0] + ".txt"
        os.chdir('../txt')
        with open(output_filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(extracted_text)
        os.chdir('..')
        print(f"Text saved in '{output_filename}'")

if __name__ == "__main__":
    main()