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

    # wait for bot to load all keys
    time.sleep(0.5)
    
    pb.answer(utils.strip2alpha(pb.data['answer'], PERMITTED_CHARS))
    pb.skip()
    pb.next()
    
    
