from crypt import methods
from re import search
from sys import prefix
from flask import Blueprint, jsonify, request
from src.settings import ks, searchLatencyHistogram

bp_search = Blueprint(name='bp_search', import_name=__name__)

@bp_search.route('/search', methods=['GET'])
@searchLatencyHistogram.time()
def search():
  prefix = request.args.get(key='prefix', default='')
  suffix = request.args.get(key='suffix', default='')
  return jsonify(ks.search(prefix, suffix))