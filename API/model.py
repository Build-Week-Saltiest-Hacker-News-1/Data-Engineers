from tensorflow.keras.models import load_model
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer

def get_predictions(comment):
    model = load_model('baseline_model.h5')
    vectorizer = pickle.load(open('tfidf.pickle'))
    prediction = model.predict(vectorizer(comment))
