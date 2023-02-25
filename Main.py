
import re
import spacy
from tkinter import*
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text_from_doc(path):
    document = Document(path)
    text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
    return text


def save_text_as_doc(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)
   
def redact_string(input_string, regex_pattern):
    redacted_string = re.sub(regex_pattern, "[REDACTED]", input_string)
    return redacted_string

def shield(input_path, output_path):
    nlp = spacy.load("en_core_web_sm")
    input_string = extract_text_from_doc(input_path)
    doc = nlp(input_string)
    vileInfo = []
    # iterate over the entities and print them
    for entity in doc.ents:
       vileInfo.append(entity.text)
    for i in vileInfo:
        input_string = input_string.replace(i, "[REDACTED]")
    save_text_as_doc(input_string, output_path)


