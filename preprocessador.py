import unicodedata
from sklearn.base import BaseEstimator, TransformerMixin

class Preprocessador(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return [self.preprocessar_texto(x) for x in X]
    def preprocessar_texto(self, texto):
        texto = str(texto).lower().strip()
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
        stopwords = {'de', 'do', 'da', 'para', 'em', 'no', 'na', 'e', 'a', 'o', 'as', 'os', 'com', 'por', 'dos', 'das'}
        palavras = [p for p in texto.split() if p not in stopwords]
        return ' '.join(palavras)
