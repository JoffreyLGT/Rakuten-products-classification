import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import nltk

from src.data.transformer import HTMLRemover, NumRemover

try:
    from nltk.corpus import stopwords
except:
    nltk.download('stopwords')
    from nltk.corpus import stopwords


class BagOfWordsDefault(Pipeline):
    def __init__(self):
        self.name = 'BagOfWordsDefault'
        steps = [
            ('remove_html', HTMLRemover()),
            ('count', CountVectorizer())
        ]
        Pipeline.__init__(self, steps)

    def get_voc(self):
        return self.steps[1][1].vocabulary_


class TfidfDefault(Pipeline):
    def __init__(self):
        self.name = 'TfidfDefault'
        steps = [
            ('remove_html', HTMLRemover()),
            ('count', CountVectorizer()),
            ('tfid', TfidfTransformer())
        ]
        Pipeline.__init__(self, steps)

    def get_voc(self):
        return self.steps[1][1].vocabulary_


class TfidfV1(Pipeline):
    def __init__(self):
        self.name = 'TfidfV1'
        self.final_stopwords_list = stopwords.words(
            'english') + stopwords.words('french') + stopwords.words('german')
        self.preproc_config_CountVect = {
            'strip_accents': 'unicode',
            'lowercase': True,
            # got from nltk (french and english)
            'stop_words': self.final_stopwords_list,
            # The lower and upper boundary of the range of n-values for different word n-grams or char n-grams
            'ngram_range': (1, 1),
            # The feature should be made of word n-gram ('word') or character n-grams (‘char’)
            'analyzer': 'word',
            'max_df': 1.,  # the vocabulary ignore terms that have a document frequency strictly higher than the given threshold
            'min_df': 0.001,  # the vocabulary ignore terms that have a document frequency strictly lower than the given threshold
            # build a vocabulary that only consider the top max_features ordered by term frequency across the corpus
            'max_features': None,
            # Mapping (e.g., a dict) where keys are terms and values are indices in the feature matrix or iterable
            'vocabulary': None
        }
        self.preproc_config_TfidfVect = {
            'norm': 'l2',
            'use_idf': True,
            'smooth_idf': True,
            'sublinear_tf': False
        }

        steps = [
            ('remove_html', HTMLRemover()),
            ('remove_num', NumRemover()),
            ('count', CountVectorizer(**self.preproc_config_CountVect)),
            ('tfid', TfidfTransformer(**self.preproc_config_TfidfVect))
        ]
        Pipeline.__init__(self, steps)

    def get_voc(self):
        return self.steps[1][1].vocabulary_
