"""Currently a bot, will become client someday"""

import requests
import websocket
import json
import pprint as pp
import time

import protobowl as pb
import utils

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ " 
ROOM = "actor-touching-chicken"
ws = websocket.WebSocket()

# connect
def connect():
    server = "ocean.protobowl.com:443/socket.io/1/websocket/"

    r = requests.get("http://"+server)
    socketString = r.text.split(":")[0]
    print("Socket = " + socketString)

    ws.connect("ws://"+server+socketString)

    # join room
    ws.send(pb.join(ROOM))

def run_bot():
    # detect new question
    while True:
        resp = ws.recv()
        if(resp.split(":::")[0] == "5"):
            q = json.loads(resp.split(":::")[1])
            
            try:
                qid = (q['args'][0]['qid'])
                answer = (q['args'][0]['answer'])

                print(answer)
                
                ws.send(pb.buzz(qid))
                ws.send(pb.guess(utils.strip2alpha(answer, PERMITTED_CHARS)))
                ws.send(pb.next_question())
                time.sleep(0.2)
            except:
                None

connect()
run_bot()

