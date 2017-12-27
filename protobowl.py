""" PB api """
# buzz time is 8 sec?

import json
import requests
import websocket
import pprint as pp
import threading
import logging
from enum import Enum

import utils

""" Main connection to PB """
class ProtoBowl:

    ws = websocket.WebSocket()
    server = 'ocean.protobowl.com:443/socket.io/1/websocket/'

    def __init__(self, room, cookie):
        # STATE VARS
        self.room_name = room
        self.cookie = cookie
        self.name = None
        self.qid = ''
        self.ans = ''
        self.users = []

        logging.basicConfig(filename='myapp.log', level=logging.INFO, filemode='w')
        #logging.getLogger().addHandler(logging.StreamHandler())

    """Reads websocket and updates vars"""
    def update(self):
        while True:

            self.ping()

            data = utils.extract_json(self.ws.recv())
            #print(json.dumps(data, indent=1))

            if type(data) is dict and data['name'] == 'sync':
                args = data['args'][0]

                try:
                    # update user info
                    if args['users']:
                        self.users = []
                        for d in args['users']:
                            u = User(
                                d['id'],
                                d['name'],
                                d['history'][-1],
                            )
                            self.users.append(u)

                except:
                    None

                # try to get question
                try:
                    self.qid = args['qid']
                    self.ans = args['answer']
                except:
                    None

    def connect(self):
        r = requests.get('http://'+self.server)
        socketString = r.text.split(':')[0]
        logging.info('Socket = ' + socketString)

        self.ws.connect('ws://'+self.server+socketString)
        self.join_room(self.cookie, self.room_name)
        logging.info('Cookie = ' + self.cookie)

        t = threading.Thread(target=self.update)
        t.start()

    def answer(self, guess):
        self.buzz()
        self.guess(guess, True)

    """ === Raw commands for interacting with PB === """
    def join_room(self, cookie, room_name):
        self.ws.send('5:::{"name":"join","args":[{"cookie":"' + cookie + '","auth":null,"question_type":"qb","room_name":"' + room_name + '","muwave":false,"agent":"M4/Web","agent_version":"Sat Sep 02 2017 11:33:43 GMT-0700 (PDT)","version":8}]}')
        logging.info('Joined ' + room_name)

    def set_name(self, name):
        self.ws.send('5:::{"name":"set_name","args":["' + name + '",null]}')
        logging.info('Set name to ' + name)

    def buzz(self):
        self.ws.send('5:23+::{"name":"buzz","args":["' + self.qid + '"]}')
        logging.info('Buzzed')

    def guess(self, guess, done=False):
        self.ws.send('5:::{"name":"guess","args":[{"text":"' + guess + '","done":true},null]}')
        logging.info('Guessed: ' + guess)

    def next(self):
        self.ws.send('5:::{"name":"next","args":[null,null]}')
        logging.info('Next')

    def skip(self):
        self.ws.send('5:::{"name":"skip","args":[null,null]}')
        logging.info('Skip')

    def pause(self):
        self.ws.send('5:::{"name":"pause","args":[null,null]}')
        logging.info('Paused')

    def unpause(self):
        self.ws.send('5:::{"name":"unpause","args":[null,null]}')
        logging.info('Unpaused')

    def ping(self):
        self.ws.send('2::')
        logging.info('Pinged!')

    def chat(self, message):
        self.ws.send('5:::{"name":"chat","args":[{"text":"'+ message +'","session":null,"first":false,"done":false},null]}')
        logging.info('Chat: ' + message)

    def set_difficulty(self, difficulty):
        self.ws.send('5:::{"name":"set_difficulty","args":["'+ difficulty.value +'",null]}')
        logging.info('Difficulty set to ' + difficulty.value)

    def set_category(self, category):
        self.ws.send('5:::{"name":"set_category","args":["'+ category.value +'",null]}')
        logging.info('Category set to ' + category.value)

""" Models a PB user """
class User:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def __str__(self):
        return 'User:' + self.id + ',' + self.name + ',' + str(self.score)

""" Difficulty enum """
class Difficulty(Enum):
    ANY     = 'Any'
    MS      = 'MS'
    HS      = 'HS'
    OPEN    = 'Open'
    COLLEGE = 'College'

""" Category enum """
class Category(Enum):
    EVERYTHING      = 'Everything'
    TRASH           = 'Trash'
    SOCIAL_SCIENCE  = 'Social Science'
    SCIENCE         = 'Science'
    RELIGION        = 'Religion'
    PHILOSOPHY      = 'Philosophy'
    MYTHOLOGY       = 'Mythology'
    LITERATURE      = 'Literature'
    HISTORY         = 'History'
    GEOGRAPHY       = 'Geography'
    FINE_ARTS       = 'Fine Arts'
    CURRENT_EVENTS  = 'Current Events'
