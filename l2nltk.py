from nltk.tokenize import word_tokenize ,sent_tokenize
from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer

s = '''Good muffins cost $.10000.\nin New York.  Please buy me
... two of them.\n\nThanks.'''
 
print(word_tokenize(s))
print(sent_tokenize(s))

nltk.download('stopwords')
#print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(s)
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

ps = PorterStemmer()
 
# choose some words to be stemmed
words = ["program", "programs", "programmer", "programming", "programmers"]
 
for w in words:
    print(w, " : ", ps.stem(w))

nltk.download('averaged_perceptron_tagger_eng') 

s = '''Good muffins cost $3.88\nin New York.  Please buy me
... two of them.\n\nThanks.'''

word_tokens = word_tokenize(s) 

tagged = nltk.pos_tag(word_tokens)
print(tagged)



from nltk.chunk import RegexpParser

#sentence = "Educative Answers is a free web encyclopedia written by devs for devs."
sentence = "BMS College for Women in New York is the best college to study BCA"


tokens = word_tokenize(sentence)

# POS tagging
pos_tags = nltk.pos_tag(tokens)

chunk_patterns = r"""
    NP: {<DT>?<JJ>*<NN>}  # Chunk noun phrases
    VP: {<VB.*><NP|PP>}  # Chunk verb phrases
"""


# chunking is a powerful tool for analyzing sentences and extracting meaningful noun and verb phrases by 
# grouping words together based on their grammar

# Create a chunk parser
chunk_parser = RegexpParser(chunk_patterns)

# Perform chunking
result = chunk_parser.parse(pos_tags)

# Print the chunked result
print(result)
result.draw()

namedEnt = nltk.ne_chunk(pos_tags, binary=False)
namedEnt.draw()