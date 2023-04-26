from flask import Flask, render_template, request  # Flask is an application
# used to run/server our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle  # pickle is used for serializing and de-serializing python object structures
import numpy as np
app=Flask(__name__)  # our flask app


@app.route('/')  # rendering the html template
def home():
    return render_template('index.html')


#  @app.route('/predict')  # rendering the html template
#  def predict():
#  return render_template("index.html")


@app.route('/predict', methods=['POST'])  # route for our prediction
def predict():
    age = request.form['age']  # requesting for age data
    gender = request.form['gender']  # requesting for gender data
    tb = request.form['tb']  # requesting for Total_Bilirubin data
    db = request.form['db']  # requesting for Direct_Bilirubin data
    ap = request.form['ap']  # requesting for Alkaline_Phosphotase data
    aa1 = request.form['aa1']  # requesting for Alamine_Aminotransferase data
    aa2 = request.form['aa2']  # requesting for Aspartate_Aminotransferase data
    tp = request.form['tp']  # requesting for Total_protiens data
    a = request.form['a']  # requesting for Albumin data
    agr = request.form['agr']  # requesting for Albumin_and_Globulin_Ratio data

    # converting data into float format
    data = [
        [float(age), float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp),
         float(a), float(agr)]]

    # loading  model which we saved
    # model = pickle.load(open('ETC.pk1', 'rb'))

    model = pickle.load(open(r'C:\Users\ELCOT\PycharmProject\flask_demo\liver analysis\ETC.pk1', 'rb'))
    prediction = model.predict(data)
    if (prediction == 1):
        return render_template('index.html', prediction='You dont have a liver disease problem')
    else:
        return render_template('index.html',
                               prediction='You have a liver disease problem, you must and should consult a doctor. Take care')


if __name__ == '__main__':
    app.run(debug=True)