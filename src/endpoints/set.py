from flask import Blueprint, jsonify, request
from src.settings import ks, keyCounter, setLatencyHistogram

bp_set = Blueprint(name='bp_set', import_name=__name__)

@bp_set.route('/set', methods=['POST'])
@setLatencyHistogram.time()
def set():
  try:
    data = request.get_json()
    ks.setitem(data)
    keyCounter.inc(amount=len(data))
    return jsonify({'success': 'true'})
  except Exception as e: 
    return jsonify({'error': 'failed to parse json'})