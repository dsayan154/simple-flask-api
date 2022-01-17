import imp
from flask import Flask, jsonify
from src.keystore import store
from src.endpoints.get import bp_get
from src.endpoints.set import bp_set
from src.endpoints.search import bp_search
from src.settings import generate
# from werkzeug.middleware.dispatcher import DispatcherMiddleware

ks = store.KeyStore()

app = Flask(__name__)

app.register_blueprint(bp_get)
app.register_blueprint(bp_set)
app.register_blueprint(bp_search)

@app.route('/metrics')
def metrics():
  return generate()
# app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
#     '/metrics': generate()
# })
