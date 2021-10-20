from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."
text = "I'm super loving you!!!"


blob = TextBlob(text)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))
'''
for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity,3))


'''

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

spanish = blob.translate(to='es')

print(spanish)

Chinese = blob.translate(to='zh')
print(Chinese)

print(Chinese.translate())


index = Word('index')

print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())


# wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())


#spellcheck and correction
word = Word('theyr')

print(word.spellcheck())

print(word.correct())


# Normalization
Word1 = Word("studies")
Word2 = Word("varieties")

print(Word1.stem())
print(Word2.stem())

print(Word1.lemmatize())
print(Word2.lemmatize())


# Definitions, synonyms and Antonyms from WordNet
happy = Word("happy")

print(happy.definitions)

print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())


synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)
