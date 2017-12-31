""" GUI WIP """
""" CURRENTLY BROKEN """

from protobowl import ProtoBowl
from protobowl import Difficulty, Category
import utils
import time
import tkinter as tk

PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
ROOM = "bot-testing"
COOKIE = utils.generate_id(PERMITTED_CHARS)

pb = ProtoBowl(ROOM, COOKIE)
pb.connect()

pb.set_name('PBot')

# UI
root = tk.Tk()
root.title('Poorman QB Client')
root.geometry('{}x{}'.format(460, 350))

# main widgets
top_frame = tk.Frame(root, bg='cyan', width=450, height=50, pady=3)
center = tk.Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = tk.Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = tk.Frame(root, bg='lavender', width=450, height=60, pady=3)

# add main widgets
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = tk.Frame(center, bg='blue', width=100, height=190)
ctr_mid = tk.Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_right = tk.Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

# Functions
def answer_key(key):
    if key.keycode == 13:
        answer()

def answer():
    pb.answer(answer_field.get())
    answer_field.delete(0, 'end')
    pb.next()

def join_room():
    pb.join_room(room_field.get())

# control widgets
answer_field = tk.Entry(btm_frame)
answer_field.bind('<Key>', answer_key)
buzzer = tk.Button(btm_frame, text='Buzz', command=answer)
next_button = tk.Button(btm_frame, text='>', command=pb.next)

room_field = tk.Entry(ctr_right)
join_button = tk.Button(ctr_right, text='Join', command=join_room)

# Add widgets
answer_field.grid(row=1, column=1)
buzzer.grid(row=1, column=2)
next_button.grid(row=1, column=3)

room_field.grid(row=1, column=1)
join_button.grid(row=2, column=1)

root.mainloop()
