import numpy as np
from flask import Flask , request , jsonify , render_template
from joblib import dump, load 



app = Flask(__name__)
app.static_folder = 'static'


model = load('Updated_DIABETESPRED.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    print(prediction[0])
    if prediction[0] == 0:
        return render_template('index.html' , prediction_text ="No , you don't have diabetes")
    else:
        return render_template('index.html' , prediction_text = "Yes, you have diabetes")

@app.route('/1') 
def home1():
    name = "Rohit"
    return render_template('Hello.php' , name = name)

if __name__ == "__main__":
    app.run(debug = True)