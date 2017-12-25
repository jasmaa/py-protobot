""" PB api """

import json
import requests
import websocket
import pprint as pp
import threading

class ProtoBowl:

    ws = websocket.WebSocket()
    server = 'ocean.protobowl.com:443/socket.io/1/websocket/'

    def __init__(self, room):
        # STATE VARS
        self.room_name = room
        self.name = None
        self.qid = ''
        self.ans = ''

    def update(self):
        while True:
            try:
                raw_data = self.ws.recv().split(':::')
                if raw_data[0] == '5':
                    self.qid = json.loads(raw_data[1])['args'][0]['qid']
                    self.ans = json.loads(raw_data[1])['args'][0]['answer']
            except:
                None
    
    def connect(self):
        r = requests.get('http://'+self.server)
        socketString = r.text.split(':')[0]
        print('Socket = ' + socketString)

        self.ws.connect('ws://'+self.server+socketString)

        self.join('batman', self.room_name)

        t = threading.Thread(target=self.update)
        t.start()
    
    def answer(self, guess):
        self.buzz(self.qid)
        self.guess(guess, True)

    """Raw commands for interacting with PB"""
    def join(self, cookie, room_name):
        self.ws.send('5:::{"name":"join","args":[{"cookie":"' + cookie + '","auth":null,"question_type":"qb","room_name":"' + room_name + '","muwave":false,"agent":"M4/Web","agent_version":"Sat Sep 02 2017 11:33:43 GMT-0700 (PDT)","version":8}]}')

    def set_name(self, name):
        self.ws.send('5:::{"name":"set_name","args":["' + name + '",null]}')

    def buzz(self, qid):
        self.ws.send('5:23+::{"name":"buzz","args":["' + qid + '"]}')

    def guess(self, guess, done):
        self.ws.send('5:::{"name":"guess","args":[{"text":"' + guess + '","done":true},null]}')

    def next(self):
        self.ws.send('5:::{"name":"next","args":[null,null]}')

    def pause(self):
        self.ws.send('5:::{"name":"pause","args":[null,null]}')

    def unpause(self):
        self.ws.send('5:::{"name":"unpause","args":[null,null]}')

    def ping(self):
        self.ws.send('2::')
