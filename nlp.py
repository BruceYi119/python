# NLP : 우리의 말을 컴퓨터에게 이해시키기 위한 분야
# 말의 의미는 단어로 구성
# 컴퓨터에게 단어의 의미를 이해시키기
# 1) 시소러스(유의어 사전):사람이 직접 단어의 의미를 정의, 뜻이 같은 단어나 뜻이 비슷한 단어를 그룹으로 분류
# 2) 통계기반
# 3) 추론기반

import nltk                                             # National Language Tollkit
from nltk.corpus import wordnet

# nltk.download('wordnet')
print(wordnet.synsets('car')[0])
c1 = wordnet.synset('car.n.01')
print('컴퓨터가 아닌 사람이 이해하는 내용', c1.definition())
print('동의어 그룹에 속한 단어들', c1.lemma_names())