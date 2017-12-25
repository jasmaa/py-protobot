"""Currently a bot, will become client someday"""

from protobowl import ProtoBowl
import utils
import time

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ " 
ROOM = "mbhsquizbowl"

pb = ProtoBowl(ROOM)
pb.connect()

pb.set_name('RedRussianBear')

while True:
    pb.answer(utils.strip2alpha(pb.ans, PERMITTED_CHARS))
    pb.next()
    pb.ping()
    time.sleep(0.1)
