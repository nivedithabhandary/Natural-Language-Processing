import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer

'''
Parts of Speech Tags:

1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
'''


train = state_union.raw("2005-GWBush.txt")
# text = state_union.raw("2006-GWBush.txt")

text = "George W Bush is the president of United States. Sky is blue and so are you."

# PunktSentenceTokenizer is a unsupervised ML tokenizer
training = PunktSentenceTokenizer(train)
tokenized_text = training.tokenize(text)

def process_content():
    try:
        for i in tokenized_text:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #print tagged
            chunk_gram = r"""Chunk: {<RB.?>*<VB.?>*<NNP.?>+<NN>?}"""

            chunkParser = nltk.RegexpParser(chunk_gram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()

    except Exception as e:
        print e

process_content()
