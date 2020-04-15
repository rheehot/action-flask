import time
from datetime import datetime
from flask import Flask, Response
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    content = 'Hello!\n%s\n%s' % (request.remote_addr, request.full_path)
    return content

@app.route('/namespace')
def hello2():
    content = 'mm-dev'
    return content


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
# Mon Oct 14 04:34:01 UTC 2019
# Mon Oct 14 04:57:49 UTC 2019
# Mon Oct 14 05:03:50 UTC 2019
# date
# change for resolve issue

