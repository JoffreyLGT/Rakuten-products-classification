from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer


class VectorizerPipeline(Pipeline):
    '''
    Create Vectorizer Pipeline constructor

    Args:
       vect_method (str): kind of vectorizer 'bag_of_words', 'tfidf'      

    Examples:
        # use case: bag_of_word with default parameters
        vect_method = 'bag_of_word'
        my_pipeline = VectorizerPipeline(vect_method)
        my_pipeline.pipe.fit(X_train.to_list())

        # use case: bag_of_word with specific parameters
        vect_method = 'bag_of_word'
        my_pipeline = VectorizerPipeline(vect_method)
        preproc_config_CountVect = {'strip_accents' : 'unicode',
                            'lowercase' : True,
                            #'stop_words' : final_stopwords_list, # got from nltk (french and english)
                            'ngram_range' : (1,1),   # The lower and upper boundary of the range of n-values for different word n-grams or char n-grams
                            'analyzer' : 'word',     # The feature should be made of word n-gram ('word') or character n-grams (‘char’)
                            'max_df' : 1., # the vocabulary ignore terms that have a document frequency strictly higher than the given threshold
                            'min_df' : 0.001, # the vocabulary ignore terms that have a document frequency strictly lower than the given threshold
                            'max_features' : None, #build a vocabulary that only consider the top max_features ordered by term frequency across the corpus
                            'vocabulary' : None # Mapping (e.g., a dict) where keys are terms and values are indices in the feature matrix or iterable
                            }
        my_pipeline.set_preproc_conf(config_CountVect=preproc_config_CountVect)
        print(my_pipeline.pipe.get_params())
        my_pipeline.pipe.fit(X_train.to_list())

        # use case: tfidf with specific parameters
        vect_method = 'tfidf'
        my_pipeline = VectorizerPipeline(vect_method)
        preproc_config_TfidfVect = {'norm' : 'l2',
                                    'use_idf' : True,
                                    'smooth_idf' : True,
                                    'sublinear_tf' : False
                                    }

        my_pipeline.set_preproc_conf(config_TfidfVect=preproc_config_TfidfVect)
        print(my_pipeline.pipe.get_params())

        my_pipeline.set_preproc_conf(config_CountVect=preproc_config_CountVect, config_TfidfVect=preproc_config_TfidfVect)
        print(my_pipeline.pipe.get_params())
    '''
    def __init__(self, vect_method):
        self.vect_method=vect_method
        self.pipe = object 
        self.preproc_config_CountVect = None
        self.preproc_config_TfidfVect = None
        
        # default parameters
        self.set_preproc_conf(self.preproc_config_CountVect, self.preproc_config_TfidfVect)

    def set_preproc_conf(self, config_CountVect=None, config_TfidfVect=None):
        ''' Set preproc and  build the pipeline
            
            Args:
                config_CountVect (dict): see Example in the class doc
                config_TfidfVect (dict): see Example in the class doc
        '''
        pipe_CountVect = []
        pipe_Tfidf = []

        if config_CountVect == None:
            pipe_CountVect = ('count', CountVectorizer())
        else:
            pipe_CountVect = ('count', CountVectorizer(**config_CountVect))

        if config_TfidfVect == None:
            pipe_Tfidf = ('tfid', TfidfTransformer())
        else:
            pipe_Tfidf = ('tfid', TfidfTransformer(**config_TfidfVect))
        

        if self.vect_method == "bag_of_word":
            # bag of word
            self.pipe = Pipeline([pipe_CountVect])
        elif self.vect_method == "tfidf":
            # tfidf
            self.pipe = Pipeline([pipe_CountVect, pipe_Tfidf])



