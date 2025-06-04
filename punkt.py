import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

text = "Ala ma kota. Kot ma na imię Mruczek."
tokens = word_tokenize(text, language='polish')
print(tokens)