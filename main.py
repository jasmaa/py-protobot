"""Currently a bot, will become client someday"""

from protobowl import ProtoBowl
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
    pb.next()
    pb.ping()
    time.sleep(0.3)
