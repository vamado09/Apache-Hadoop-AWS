import joblib
import os
import pandas as pd
import json
from io import StringIO


def model_fn(model_dir):
    model_file = os.path.join(model_dir, "model1.joblib")
    model = joblib.load(model_file)
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "text/csv":
        data = pd.read_csv(StringIO(request_body))
        return data
    else:
        raise ValueError("Unsupported content type: " + str(request_content_type))

def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction

def output_fn(prediction, response_content_type):
    if response_content_type == "text/csv":
        return pd.DataFrame(prediction).to_csv(header=False, index=False)
    elif response_content_type == "application/json":
        return json.dumps(prediction.tolist())  # Convert prediction to JSON
    else:        
        raise ValueError("Unsupported response content type: " + str(response_content_type))

