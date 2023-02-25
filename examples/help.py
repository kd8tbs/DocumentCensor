import spacy

# Load the Spacy model
nlp = spacy.load('en_core_web_sm')

# The text string containing sensitive and identifiable information
text = "John Smith's Social Security Number is 123-45-6789. He was born on January 1st, 1980 and has a bank account with a balance of $10,000. His mother's maiden name is Johnson."

# Process the text string using Spacy
doc = nlp(text)

# Define a set of sensitive and identifiable entities
sensitive_entities = {'PERSON', 'ORG', 'GPE', 'DATE', 'MONEY'}

# Extract sensitive and identifiable information from the text string
sensitive_info = set()
for ent in doc.ents:
    if ent.label_ in sensitive_entities:
        sensitive_info.add((ent.text, ent.label_))
        
for token in doc:
    if token.ent_type_ in sensitive_entities:
        sensitive_info.add((token.text, token.ent_type_))
    elif token.pos_ == 'PROPN':
        sensitive_info.add((token.text, 'PROPN'))
    elif token.pos_ == 'NOUN' and token.dep_ == 'compound':
        sensitive_info.add((token.text, 'COMPOUND_NOUN'))

# Print the sensitive and identifiable information
print(sensitive_info)
