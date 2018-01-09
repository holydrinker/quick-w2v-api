from flask import Flask
from flask import jsonify
from model_loader import load

model_name = "model.bin"
model = load(model_name)

app = Flask(__name__)


@app.route('/vec/<term>')
def vec(term):
    return jsonify('vec', model[term].tolist())
