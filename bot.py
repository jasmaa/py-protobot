""" Bot example """

from client.protobowl import ProtoBowl
from client.protobowl import Difficulty, Category
import client.utils as utils
import time

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
ROOM = "bot-testing-c"
COOKIE = utils.generate_id(PERMITTED_CHARS)

pb = ProtoBowl(ROOM, COOKIE)
pb.connect()

pb.set_name('PBot')

while True:
    # wait to load all keys
    pb.unpause()
    pb.skip()
    pb.next()
    time.sleep(0.5)
    pb.answer(utils.strip2alpha(pb.data['answer'], PERMITTED_CHARS))
