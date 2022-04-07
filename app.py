import os.path
from collections import OrderedDict
from flask import Flask, request, json, make_response
from werkzeug.exceptions import HTTPException
from flask import jsonify
import pickle
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({"status": e.code})
    response.content_type = "application/json"
    return response

@app.route('/input', methods=["POST"])
def path():
    if os.path.exists("Naive_Division_Model.sav") == True:
        if os.path.exists("Naive_Division_Vectorizer.sav") == True:
            # return {"success": "run input!"}
            return input()
        else:
            return {"error": "Missing file: Naive_Division_Vectorizer.sav"}
    else:
        return {"error": "Missiong file: Naive_Division_Model.sav"}

def input():
    remark = request.args.get("remark")
    
    if len(remark.split()) < 10:
        return {"error": "Please write a remark with a minimum word count is 10!"}
    else:
        return text_processing(remark)
    
def text_processing(remarks):
    clean_remark = remarks.\
        lower().\
        replace('\d+', ' ').\
        replace(r'[[:punct:]]', ' ').\
        replace('\r\n', ' ').\
        replace('\\b[a-z]\\b', ' ').\
        replace('\W+', ' ').\
        replace(' +', ' ')
        
    clean_remark = StemmerFactory().create_stemmer().stem(clean_remark)
    
    return predict(clean_remark)

def predict(remarks):
    model_div = pickle.load(open("Naive_Division_Model.sav", "rb"))
    vect_div = pickle.load(open("Naive_Division_Vectorizer.sav", "rb"))

    model_target = pickle.load(open("Naive_Target_Model.sav", "rb"))
    vect_target = pickle.load(open("Naive_Target_Vectorizer.sav", "rb"))

    model_tar_3 = pickle.load(open("Naive_3_Model.sav", "rb"))
    vect_tar_3 = pickle.load(open("Naive_3_Vectorizer.sav", "rb"))
    model_tar_4 = pickle.load(open("Naive_4_Model.sav", "rb"))
    vect_tar_4 = pickle.load(open("Naive_4_Vectorizer.sav", "rb"))
    model_tar_5 = pickle.load(open("Naive_5_Model.sav", "rb"))
    vect_tar_5 = pickle.load(open("Naive_5_Vectorizer.sav", "rb"))
    model_tar_6 = pickle.load(open("Naive_6_Model.sav", "rb"))
    vect_tar_6 = pickle.load(open("Naive_6_Vectorizer.sav", "rb"))
    model_tar_7 = pickle.load(open("Naive_7_Model.sav", "rb"))
    vect_tar_7 = pickle.load(open("Naive_7_Vectorizer.sav", "rb"))
    model_tar_8 = pickle.load(open("Naive_8_Model.sav", "rb"))
    vect_tar_8 = pickle.load(open("Naive_8_Vectorizer.sav", "rb"))
    model_tar_9 = pickle.load(open("Naive_9_Model.sav", "rb"))
    vect_tar_9 = pickle.load(open("Naive_9_Vectorizer.sav", "rb"))
    model_tar_10 = pickle.load(open("Naive_10_Model.sav", "rb"))
    vect_tar_10 = pickle.load(open("Naive_10_Vectorizer.sav", "rb"))
    
    rmrk = OrderedDict(remarks=remarks)
    div = OrderedDict(division=str(model_div.predict(vect_div.transform([remarks]))[0]))
    target = OrderedDict(difficulty=str(model_target.predict(vect_target.transform([remarks]))[0]))

    if model_target.predict(vect_target.transform([remarks]))[0] == 3:
        point = OrderedDict(point=str(model_tar_3.predict(vect_tar_3.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 4:
        point = OrderedDict(point=str(model_tar_4.predict(vect_tar_4.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 5:
        point = OrderedDict(point=str(model_tar_5.predict(vect_tar_5.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 6:
        point = OrderedDict(point=str(model_tar_6.predict(vect_tar_6.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 7:
        point = OrderedDict(point=str(model_tar_7.predict(vect_tar_7.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 8:
        point = OrderedDict(point=str(model_tar_8.predict(vect_tar_8.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 9:
        point = OrderedDict(point=str(model_tar_9.predict(vect_tar_9.transform([remarks]))[0]))
    elif model_target.predict(vect_target.transform([remarks]))[0] == 10:
        point = OrderedDict(point=str(model_tar_10.predict(vect_tar_10.transform([remarks]))[0]))

    result = OrderedDict(status=200, data=rmrk|div|target|point)
    return result

if __name__ == '__main__':
    app.run(debug=True)