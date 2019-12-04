import boto3
from chalice import Chalice
from chalice import Response
import json
import pandas as pd


db = boto3.resource('dynamodb', region_name='us-east-2')
table = db.Table('ShoutOuts')
data = table.scan()
app = Chalice(app_name='demo')


@app.route('/')
def index():
    data = table.scan()
    df = pd.DataFrame(data['Items'])
    cols = ['name', 'msg']
    df = df[cols].copy()
    body = df.to_html()
    return  Response(body=body,
            status_code=200,
            headers={'Content-Type': 'text/html'})



@app.route('/shouts', methods=['GET'])
def get_shouts():
    data = table.scan()
    print(data)
    return data['Items']


@app.route('/shout/{name}', methods=['GET'])
def get_shout(name):
    data = table.get_item(Key=name)
    print(data)
    return data['Item']


@app.route('/shout/{name}', methods=['POST'])
def shout(name):
    shout_out = app.current_request.raw_body.decode('utf-8')
    try:
        item = json.loads(shout_out)
    except:
        item = {"msg": str(shout_out).strip()}
    item['name'] = name
    r = table.put_item(Item=item)
    print(r)
    return {'ack': True}

