from distutils.log import error
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/lusiadas_chants"
mongo = PyMongo(app)


@app.route("/chant/<chant_number>/<stranza>")
def get_chant(chant_number, stranza):
    if chant_number.isdigit() == False or stranza.isdigit() == False:
        return jsonify(error=500, text="Parâmetros inválidos"), 500    
    
    chant = mongo.db.chant.find_one({"chant_number": int(chant_number), "stranza": int(stranza)})
    if chant:
        chant = dumps(chant) 
        return chant

    return jsonify(error=500, text="Canto não encontrado"), 500