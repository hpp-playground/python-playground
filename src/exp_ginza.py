import spacy
from spacy.lang.ja import Japanese
from spacy.tokens.doc import Doc

nlp: Japanese = spacy.load("ja_ginza")
doc: Doc = nlp("赤い車を持っている")
for tkn in doc:
    print(tkn.i, tkn.orth_, tkn.lemma_, tkn.pos_, tkn.tag_, tkn.dep_, tkn.head.i)

