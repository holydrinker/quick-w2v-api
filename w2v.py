from flask import Flask, request
from flask import jsonify
from model_loader import load

model_name = "model.bin"
model = load(model_name)

app = Flask(__name__)


@app.route('/vec/<term>')
def vec(term):
    return jsonify(model[term].tolist())


@app.route('/vecs', methods=['POST'])
def vecs():
    if request.method == 'POST':
        terms = request.get_json()
        w2vecs = [model[term].tolist() for term in terms]
        return jsonify(w2vecs)
    return 'Only post request allowed'
