import protobowl
import client
import time

pb = protobowl.ProtoBowl('bot-testing-two', 'cookie')
pb.connect()
pb.set_name('pbot-client')

print('init question display')
q_disp = client.QuestionDisplay(pb)
