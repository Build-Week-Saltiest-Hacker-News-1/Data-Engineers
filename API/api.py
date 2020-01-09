from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer

def create_app():
    app = Flask(__name__)

    @app.route("/predictor", method=["POST"])

    def predictor():
        from_backend = request.get_json(Force=True)

        iidd = from_backend['id']
        comment = from_backend['comment']
        user_name = from_backend['user_name']

        model = load_model('baseline_model.h5')
        vectorizer = pickle.load(open('tfidf.pickle'))
        predictions = model.predict(vectorizer(comment))

        answer = {'id': iidd, 'prediction': predictions}

        

        return jsonify(answer)
    
    return app

