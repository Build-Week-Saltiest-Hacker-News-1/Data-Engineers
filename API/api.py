from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer
import os




def create_app():
    app = Flask(__name__)


    @app.route("/predictor", methods=["POST"])
    def predictor():
        from_backend = request.get_json(force=True)

        iidd = from_backend['comment_id']
        comment = from_backend['SaltyComment']
        # user_name = from_backend['user_name']

        
        model = load_model('./API/baseline_model_v2.h5')
        vectorizer = pickle.load(open('./API/tfidf_v2.pickle', 'rb'))

        predictions = model.predict(vectorizer.transform([comment]).toarray())
        predictions = predictions.tolist()

        answer = {'comment_id': iidd, 'saltyRank': predictions[0][0]}

        return jsonify(answer)
    
    return app
