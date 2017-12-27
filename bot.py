""" Bot example """

from protobowl import ProtoBowl
from protobowl import Difficulty, Category
import utils
import time

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
ROOM = "bot-testing"
COOKIE = utils.generate_id(PERMITTED_CHARS)

pb = ProtoBowl(ROOM, COOKIE)
pb.connect()

pb.set_name('PBot')

while True:
    
    
    pb.answer(utils.strip2alpha(pb.ans, PERMITTED_CHARS))
    pb.skip()
    pb.next()

    time.sleep(0.3)
