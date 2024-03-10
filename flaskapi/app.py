from flask import Flask, request,render_template,json
import joblib
import pandas as pd


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route('/predict',methods=[" GETpython","POST"])
def predict():
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    df = data_validation(df)

    with open("log_model.pkl", 'rb') as file:
        log_reg = joblib.load(file)
    predictions_test = log_reg.predict(df)

    df['Predicted Churned Customers'] = predictions_test
    return df.to_json(orient="split")

def data_validation(df):
     # some logic
     return df

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
