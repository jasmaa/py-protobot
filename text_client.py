import protobowl
import client
import time

pb = protobowl.ProtoBowl('bot-testing-two', 'cookie')
pb.connect()
pb.set_name('pbot-client')

time.sleep(0.1)

print('init client')
cl = client.Client(pb)
