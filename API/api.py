from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer

def create_app():
    app = Flask(__name__)

    @app.route("/predictor", methods=["POST"])
    def predictor():
        from_backend = request.get_json(force=True)

        iidd = from_backend['comment_id']
        comment = from_backend['comment']
        # user_name = from_backend['user_name']

        model = load_model('API\\baseline_model.h5')
        vectorizer = pickle.load(open('API\\tfidf.pickle', 'rb'))
        predictions = model.predict(vectorizer.transform([comment]))
        predictions = predictions.tolist()

        answer = {'id': iidd, 'prediction': predictions[0][0]}

        return jsonify(answer)
    
    return app
