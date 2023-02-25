import PyPDF2
import re
from tkinter import*
from PyPDF2 import PdfReader
from PyPDF2 import PageObject, PdfReader
import spacy
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(path):
    """
    Extracts all text from a PDF file and returns it as a string.
    """
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


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


def redact_string(input_string, regex_pattern):
    redacted_string = re.sub(regex_pattern, "[REDACTED]", input_string)
    #print(redacted_string)
    return redacted_string

def shield(input_path, output_path):
    text = extract_text_from_pdf(input_path)
    # apply the language model to extract named entities
    doc = nlp(text)

    # iterate over the entities and print them
    for entity in doc.ents:
        print(entity.text, entity.label_)

        
    save_text_as_pdf("text", input_path, output_path)
    



