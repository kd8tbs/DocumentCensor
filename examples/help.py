import spacy

# load the language model
nlp = spacy.load("en_core_web_sm")

# define the string to analyze
input_string = "Hello world, my name is Poony or Daniel. My phone number for local single women is (989)842-7702. If needed my routing number for sending money 123456789. My current Address South 9 Mile road in Midland Michigan. My birthday is 11/20/1999. My driver license D550372760888. My social security is 123-12-1234 Create backstory on why this would be beneficial for businesses or regular citizens. Don’t sell the product, create a way to show how it will be helpful for the future and how data will be protected."

# apply the language model to extract named entities
doc = nlp(input_string)

# iterate over the entities and print them
for entity in doc.ents:
    print(entity.text, entity.label_)