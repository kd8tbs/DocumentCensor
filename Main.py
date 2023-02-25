import PyPDF2
from PyPDF2 import PageObject, PdfReader
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

import PyPDF2

def save_text_as_pdf(text, template_path, file_name):
    # open the existing PDF template
    with open(template_path, 'rb') as template_file:
        # create a PyPDF2 PdfFileReader object from the template
        template_pdf = PyPDF2.PdfReader(template_file)
        
        # create a new PDF document
        output_pdf = PyPDF2.PdfWriter()
        
        # loop through each page of the template and add it to the output PDF
        for i in range(len(template_pdf.pages)):
            page = template_pdf.pages[i]
            output_pdf.add_page(page)
        
        # create a new page and add the text to it
        new_page = PageObject.create_blank_page(None, output_pdf.pages[0].mediabox.width, output_pdf.pages[0].mediabox.height)
        new_page.merge_page(output_pdf.pages[0])
        # content_stream = PyPDF2.pdf.ContentStream([PyPDF2.pdf.TextObject.createTextObject(output_pdf, text)], new_page)
        # new_page._contentStreams = [content_stream]
        output_pdf.add_page(new_page)
        
        # save the output PDF to a file
        with open(file_name, 'wb') as output_file:
            output_pdf.write(output_file)


    

def tokenize(text):
    """Tokenizes a string based on words.

    Args:
        text (str): The input string to tokenize.

    Returns:
        list: A list of words in the input string.
    """
    tokens = text.split()
    return tokens

def detokenize(tokens):
    """Detokenizes a list of words into a string.

    Args:
        tokens (list): A list of words to detokenize.

    Returns:
        str: A string of words.
    """
    return ' '.join(tokens)


def redact_strings(arr, regex_filter):
    """ 
    Redacts strings in an array that match a regex filter.

    Parameters:
    arr (list): An array of strings
    regex_filter (str): A regex pattern to filter the strings

    Returns:
    list: A modified array where strings matching the regex filter are replaced with "[REDACTED]"
    """
    print(regex_filter)
    redacted_arr = []
    for string in arr:
        if re.search(regex_filter, string):
            redacted_arr.append("[REDACTED]")
            print('Redacted: ' + string)
        else:
            redacted_arr.append(string)
            print('Not Redacted: ' + string)
    return redacted_arr

if __name__ == '__main__':
    # main stuff goes here
    text = extract_text_from_pdf('examples/test.pdf')
    save_text_as_pdf(text, 'examples/test.pdf', 'examples/output.pdf')