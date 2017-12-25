import requests
import websocket
import json

def build_join(room):

    data = {}
    data['name'] = 'join'

    args = {}
    args['cookie'] = 'PB4CLsdc5gkhwvnqt8ugkplo3t4e9qeqco679v2s1'
    args['auth'] = None
    args['question_type'] = 'qb'
    args['muwave'] = False
    args['agent'] = 'M4/Web'
    args['agent_version'] = 'Sat Sep 02 2017 11:33:43 GMT-0700 (PDT)'
    args['version'] = 8

    data['args'] = args

    return '5::: ' + json.dumps(data)

# connect
server = "ocean.protobowl.com:443/socket.io/1/websocket/"

r = requests.get("http://"+server)
socketString = r.text.split(":")[0]
print("Socket = " + socketString)

ws = websocket.WebSocket()
ws.connect("ws://"+server+socketString)
while True:
    ws.send(build_join("direac-arousing-chicken"))
    print(ws.recv())
