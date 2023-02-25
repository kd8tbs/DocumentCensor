import PyPDF2
from PyPDF2 import PdfReader
import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
import re

def extract_text_from_pdf(path):
    """
    Extracts all text from a PDF file and returns it as a string.
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def create_pdf_with_text(text, input_path, output_path):
    # Open the original PDF file
    with open(input_path, 'rb') as f:
        pdf = PdfReader(f)

        # Create a new PDF writer
        writer = PdfWriter()

        # Add the document information to the new PDF writer
        writer.add_metadata(pdf.metadata)

        # Add each page from the original PDF to the new PDF writer
        for page_num in range(len(pdf.pages)):
            # page = pdf.getPage(page_num)
            page = pdf.pages[page_num]
            writer.add_page(page)

        # Add a new page with the extracted text
        new_page = writer.add_blank_page(width=200, height=200) # Change the width and height to suit your needs
        new_page.merge_page(PdfReader(BytesIO(text.encode())).getPage(0))
        new_page.mergeTranslatedPage(new_page, dx=0, dy=100, expand=False) # Change the dx and dy values to adjust the position of the added text

        # Write the new PDF to a BytesIO buffer
        output_buffer = BytesIO()
        writer.write(output_buffer)

    # Write the BytesIO buffer to the output file
    with open(output_path, 'wb') as f:
        f.write(output_buffer.getvalue())

    

def tokenize(text):
    """Tokenizes a string based on words.

    Args:
        text (str): The input string to tokenize.

    Returns:
        list: A list of words in the input string.
    """
    tokens = text.split()
    return tokens


def redact_strings(arr, regex_filter):
    """ 
    Redacts strings in an array that match a regex filter.

    Parameters:
    arr (list): An array of strings
    regex_filter (str): A regex pattern to filter the strings

    Returns:
    list: A modified array where strings matching the regex filter are replaced with "[REDACTED]"
    """
    redacted_arr = []
    for string in arr:
        if re.search(regex_filter, string):
            redacted_arr.append("[REDACTED]")
        else:
            redacted_arr.append(string)
    return redacted_arr

if __name__ == '__main__':
    # main stuff goes here
    text = extract_text_from_pdf('examples/SensitiveInfo.pdf')
    # create_pdf_with_text(extract_text_from_pdf('examples/test.pdf'), 'examples/test.pdf', 'examples/test2.pdf') # TODO: Fix this
    regex_arr = [
    r"\d\d\d-\d\d-\d\d\d\d",  # Social Security 123-12-1234
    r"\d\d/\d\d/\d\d\d\d",  # Birthdays 11/30/1980
    r"^[A-Za-z]{2}\d{2}-\d{5}-\d{4}$",  # Driver License Numbers D123456789123
    r"\d\d\d\d\d\d\d\d\d",  # Routing Number 123456789
    r"\(\d\d\d\)\d\d\d-\d\d\d\d" #Phone Numbers (231)667-503
    ]
    tokenized_text = tokenize(text)
    
    for regex in regex_arr:
        print(regex)
        tokenized_text = redact_strings(tokenized_text, regex)
    
    print(tokenized_text)
    arr = ["password123", "user123", "admin", "admin123", "(989)842-7702"]
    regex_filter = r"^\(\d{3}\)\d{3}-\d{4}$"

    redacted_arr = redact_strings(arr, regex_filter)

    print(redacted_arr) # prints ["[REDACTED]", "user123", "[REDACTED]", "[REDACTED]"]


    
