import nltk
nltk.download("stopwords")
nltk.download("punkt")

from sklearn.metrics.pairwise import cosine_distances, cosine_similarity
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer

sw_indo = stopwords.words("indonesian") + list(punctuation)
