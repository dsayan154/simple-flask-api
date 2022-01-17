from re import search
from src.keystore import store
from prometheus_client import Counter, Histogram, generate_latest, make_wsgi_app

ks = store.KeyStore()
keyCounter = Counter('keys', 'Total number of keys in DB')
# statusCodesGauge = Gauge('http_status_code', 'HTTP status code of the endpoints', ['get', 'set', 'search'])
latencyHistogram = Histogram('response_latency', 'Response latency of the endpoints', ['endpoint'])
setLatencyHistogram = latencyHistogram.labels('/set')
getLatencyHistogram = latencyHistogram.labels('/get')
searchLatencyHistogram = latencyHistogram.labels('/search')

def generate():
  return make_wsgi_app()