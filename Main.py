import PyPDF2
from PyPDF2 import PdfReader

def extract_text_from_pdf(path):
    """
    Extracts all text from a PDF file and returns it as a string.
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def insert_text_into_pdf(path, text):
    """
    Inserts text into a PDF file and saves the updated file.
    """
    # Open the PDF file in read-binary mode.
    with open(path, 'rb') as file:
        # Create a PDF reader object.
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Create a PDF writer object.
        pdf_writer = PyPDF2.PdfFileWriter()

        # Get the number of pages in the PDF file.
        num_pages = pdf_reader.getNumPages()

        # Iterate through all the pages and add the text.
        for page in range(num_pages):
            # Get the current page object.
            pdf_page = pdf_reader.getPage(page)

            # Add the text to the page.
            pdf_page.mergePage(PyPDF2.pdf.PageObject.createTextObject(text))

            # Add the updated page to the writer.
            pdf_writer.addPage(pdf_page)

        # Save the updated PDF file.
        with open(path, 'wb') as output:
            pdf_writer.write(output)

    
    

def tokenize(text):
    """Tokenizes a string based on words.

    Args:
        text (str): The input string to tokenize.

    Returns:
        list: A list of words in the input string.
    """
    tokens = text.split()
    return tokens



if __name__ == '__main__':
    # main stuff goes here
    print(extract_text_from_pdf('examples/test.pdf'))
    # insert_text_into_pdf('examples/test2.pdf', 'Hello World')