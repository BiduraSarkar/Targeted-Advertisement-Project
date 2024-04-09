from flask import Flask,request,render_template 
import numpy as np
import pickle
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    
    if request.method == 'POST':
     dts = float(request.form.get("dts"))
     age = float(request.form.get("age"))
     ai = float(request.form.get("ai"))
     dia = float(request.form.get("dia"))
     ad_name = int(request.form.get("ad_name"))
     city = int(request.form.get("city"))
     gender = int(request.form.get("gender"))
     time = int(request.form.get("time"))
     arr = np.array([dts,age,ai,dia,ad_name,city,gender,time])
     
     with open('classifier.pkl','rb') as file:
        clf = pickle.load(file)
        pred = clf.predict([arr])
        if pred[0]==1:
           return "<h1>Person will click on add<h1>"
        elif pred[0]==0:
           return "<h1>Person will not click on add<h1>"
    
    return render_template("home.html")

if __name__ == '__main__':
   app.run()