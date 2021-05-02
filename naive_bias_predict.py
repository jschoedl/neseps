import pickle

import nltk
import os

nltk.download('punkt')
LABELS = "toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"
CURRENT_DIR = "/".join(__file__.split("/")[:-1])


def predict(data):
    res = {
        'results': dict(),
        'errors': [],
        'warnings': [],
    }

    for label in LABELS:
        try:
            try:
                with open(f"{CURRENT_DIR}/models/{label}.pickle", "rb") as f:
                    vectorizer, model = pickle.load(f)
            except OSError as e:
                res['errors'].append(f"could not load model for label '{label}': {e}")
            except Exception as e:
                res['errors'].append(f"unknown exception while loading label '{label}': {e}")
            else:
                y_pred = model.predict(vectorizer.transform(data))
                res['results'][label] = y_pred
        except Exception as e:
            res['errors'].append(f"unknown exception while processing label '{label}': {e}")
    return res
