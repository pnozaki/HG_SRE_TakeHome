from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE'])
def home_page():
    method = request.method
    uri = request.path
    app.logger.info("{'method' : '%s' , 'uri' : '%s'}", method, uri)
    return "<h1>Healthgrades SRE API code challenge</h1><p>Welcome to the API</p>"

@app.route('/<path:fake>', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE'])
def all(fake):
    return home_page()

if __name__ == '__main__':
    logFormatStr = ()
    logging.basicConfig(format=logFormatStr, filename=r'/var/log/log-{:%Y-%m-%d}.txt'.format(datetime.now()), level=logging.INFO)
    app.run(debug=False, host='0.0.0.0', port=3000)
