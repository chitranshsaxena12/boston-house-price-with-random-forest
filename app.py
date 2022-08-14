from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app=Flask(__name__,template_folder='template')
model = pickle.load(open('finalized_model.pickle', 'rb'))
@app.route("/",methods=["GET"])
def Home_page():
    return render_template("index.html")


standard_to = StandardScaler()
@app.route("/predict",methods=["POST"])
def prediction_page():
    if request.method == "POST":
        LSTAT = float(request.form["LSTAT"])
        INDUS = float(request.form["INDUS"])
        NOX = float(request.form["NOX"])
        PTRATIO = float(request.form["PTRATIO"])
        RM = float(request.form["RM"])
        TAX = float(request.form["TAX"])
        DIS = float(request.form["DIS"])
        AGE = float(request.form["AGE"])

        prediction = model.predict([[ LSTAT,INDUS, NOX, PTRATIO, RM, TAX, DIS, AGE]])
        return render_template('result.html',result=prediction)

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)




