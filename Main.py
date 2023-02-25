
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
      # Load the English language model

    # Process the text with spaCy
    text = extract_text_from_doc(input_path)
    doc = nlp(text)

    # Define a list of sensitive entity types to look for
    sensitive_entities = ["NAME", "DATE", "TIME", "MONEY", "CREDIT_CARD", "SSN"]

    # Create a list to store the sensitive entities
    sensitive_info = []

    # Iterate over the entities in the document
    for ent in doc.ents:
        # Check if the entity type is sensitive
        
        if ent.label_ in sensitive_entities:
            # Add the sensitive entity text and label to the list
            sensitive_info.append((ent.text, ent.label_))
            print(sensitive_info)
    # Return the list of sensitive entities
    save_text_as_doc(text, output_path)


