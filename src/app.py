import imp
from flask import Flask, jsonify
from src.keystore import store
from src.endpoints.get import bp_get
from src.endpoints.set import bp_set
from src.endpoints.search import bp_search
from src.settings import generate

ks = store.KeyStore()

app = Flask(__name__)

app.register_blueprint(bp_get)
app.register_blueprint(bp_set)
app.register_blueprint(bp_search)

@app.route('/metrics')
def metrics():
  # print(generate().decode(encoding='utf-8'))
  return generate().decode(encoding='utf-8').splitlines()
