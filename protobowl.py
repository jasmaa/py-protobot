"""Commands for interacting with PB"""

import json

def join(room):

    data = {}
    data['name'] = 'join'

    args = {}
    args['cookie'] = 'asdf'
    args['auth'] = None
    args['question_type'] = 'qb'
    args['room_name'] = room
    args['muwave'] = False
    args['agent'] = 'M4/Web'
    args['agent_version'] = 'Sat Sep 02 2017 11:33:43 GMT-0700 (PDT)'
    args['version'] = 8
    data['args'] = args

    return '5:::' + json.dumps(data)

def buzz(qid):
    data = {}

    data['name'] = 'buzz'
    args = [1]
    args[0] = qid
    
    data['args'] = args

    return "5:23+::" + json.dumps(data)

def guess(guess):
    data = {}
    data['name'] = 'guess'

    args = [2]
    arg_data = {}
    arg_data['text'] = guess
    arg_data['done'] = True

    args[0] = arg_data
    data['args'] = args

    return '5:::' + json.dumps(data)

def next_question():
    data = {}

    data['name'] = 'next'
    args = [2]

    data['args'] = args

    return "5:::" + json.dumps(data)
