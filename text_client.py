""" Text client example """

from client.protobowl import ProtoBowl
from client.display import QuestionDisplay
import time

pb = ProtoBowl('bot-testing-vr', 'cookie')
pb.connect()
pb.set_name('pbot-client')

print('init question display')
q_disp = QuestionDisplay(pb)
