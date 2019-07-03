import textblob
from textblob import TextBlob


def POSTag(sentences): 
    wiki = TextBlob(sentences)
    return wiki.tags


# print(POSTag('I love you'))
