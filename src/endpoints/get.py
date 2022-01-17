from flask import Blueprint, jsonify
from src.settings import ks, latencyHistogram

bp_get = Blueprint(name="bp_get", import_name=__name__)

@bp_get.route('/get/<string:key>', methods=['GET'])
@latencyHistogram.time()
def get(key):
  resp = {}
  try:
    value = ks.getitem(key)
    if type(value) == KeyError:
      raise KeyError
    resp = {str(key): value}
    print(resp)
  except KeyError:
    resp = {'error': f'{key} not found'} 
  return jsonify(resp)
