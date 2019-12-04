from chalice import Chalice
import json


app = Chalice(app_name='demo')
shoutouts = {}


@app.route('/')
def index():
    return shoutouts


@app.route('/shout/{name}', methods=['GET'])
def get_shout(name):
    return shoutouts[name]


@app.route('/shout/{name}', methods=['POST'])
def shout(name):
    shout_out = app.current_request.raw_body.decode('utf-8')
    try:
        item = json.loads(shout_out)
    except:
        item = str(shout_out).strip()
    shoutouts[name] = item
    return {'ack': True}

