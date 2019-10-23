from __future__ import print_function
from gensim.models import KeyedVectors

pt_model = KeyedVectors.load_word2vec_format('/home/rubens/Downloads/wiki.pt.vec')

words = []
for word in pt_model.vocab:
    words.append(word)

get_similar = 'customizar'

pt_model.most_similar(positive=get_similar,topn=30)
    
word_plus = ['homem', 'rei']
word_minus = ['poder']

# Necessary to clean the similarity result

# ** ALSO: Necessary to LEMMATIZE sentences to match proper similarity

pt_model.most_similar(positive=word_plus, negative=word_minus)

#################################################################

pt_model.most_similar(positive="customizar",topn=30)

[('customiza', 0.9207000732421875),
 ('customizando', 0.8824794292449951),
 ('customizam', 0.8791165351867676),
 ('customize', 0.8624278903007507),
 ('customização', 0.8487346172332764),
 ('customizado', 0.8440653681755066),
 ('customizada', 0.8424166440963745),
 ('customizações', 0.8347393870353699),
 ('customizadas', 0.8307189345359802),
 ('customizados', 0.827279806137085),
 ('customizou', 0.8249801397323608),
 ('customizáveis', 0.8122011423110962),
 ('customizable', 0.807347297668457),
 ('customizável', 0.7967360615730286),
 ('customized', 0.7433868646621704)]
