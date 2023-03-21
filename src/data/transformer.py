from html.parser import HTMLParser
from sklearn.base import BaseEstimator, TransformerMixin


class HTMLRemover(BaseEstimator, TransformerMixin):
    """"
    Transformer removing HTML tags and decoding HTML special characters.
    """

    def _parseValue(self, value):
        if type(value) != str:
            return value
        parser = _RakutenHTMLParser()
        parser.feed(value)
        return parser.get_all_content()

    def _parseColumn(self, column):
        return [self._parseValue(value) for value in column]

    def fit(self, X, y):
        # Do nothing, mandatory function for when a model is provided to the pipeline.
        return self

    def transform(self, X):
        return X.apply(lambda column: self._parseColumn(column))


class _RakutenHTMLParser(HTMLParser):
    """
    Parse the text fed to it using feed() and return the content without HTML tag or encoding with get_all_content().
    """

    def __init__(self):
        self.allcontent = ""
        super(_RakutenHTMLParser, self).__init__()

    def handle_data(self, data):
        self.allcontent += data + " "

    def get_all_content(self):
        return self.allcontent.strip()
