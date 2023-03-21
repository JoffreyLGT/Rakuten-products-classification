import numpy as np
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import scipy.sparse as sparse

class TextPreprocess():
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def fit(self, data) -> object:
        return self.pipeline.fit(data)
        
    def transform(self, data) -> np.array:
        return self.pipeline.transform(data)

    def save(self, data, prefix_filename):
        data_sparse = sparse.csr_matrix(data)
        file_name = f"{prefix_filename}_{self.pipeline.name}.pkl"
        with open(file_name,'wb') as fp:
            pickle.dump(data_sparse, fp)

    def save_voc(self, prefix_filename):
        voc = self.pipeline.get_voc()
        print(voc)
        file_name = f"{prefix_filename}_{self.pipeline.name}.pkl"
        with open(file_name,'wb') as fp:
            pickle.dump(voc, fp)

