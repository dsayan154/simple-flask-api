import os
from sys import prefix
import requests

def test_bp_set_get_test1(api_v1_host):
  endpoint = os.path.join(api_v1_host, 'set')
  payload = {'abc-1': 'abcval1', 'abc-2': 'abcval2', 'xyz-1': 'xyzval1', 'xyz-2': 'xyzval2', 'xyz1': 'xyzval3'}
  response = requests.post(endpoint, json=payload)
  assert response.status_code == 200
  json = response.json()
  assert 'success' in json
  assert json['success'] == 'true'
  
def test_bp_get_test1(api_v1_host):
  key = 'abc-1'
  endpoint = os.path.join(api_v1_host, 'get', key)
  response = requests.get(endpoint)
  assert response.status_code == 200
  json = response.json()
  assert key in json
  assert json[key] == 'abcval1'

def test_bp_get_test2(api_v1_host):
  key = 'doesnotexist'
  endpoint = os.path.join(api_v1_host, 'get', key)
  response = requests.get(endpoint)
  assert response.status_code == 200
  json = response.json()
  assert 'error' in json
  assert json['error'] == f'{key} not found'

def test_bp_search_test1(api_v1_host):
  endpoint = os.path.join(api_v1_host, 'search?prefix=x&suffix=1')
  response = requests.get(endpoint)
  assert response.status_code == 200
  json = response.json()
  assert json == ['xyz-1', 'xyz1']
