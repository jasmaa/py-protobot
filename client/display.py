""" Client-side code """

from client.protobowl import GameState
import time
import threading

""" Class for tracking and syncing questions """
class QuestionDisplay:
    def __init__(self, pb):
        # Wait for main pb client to start up
        time.sleep(0.5)

        self.pb = pb
        self.local_time = 0
        self.local_index = 0
        self.disp = ''

        self.init_disp()

        update_disp_t = threading.Thread(target=self.update_disp)
        update_disp_t.start()

        debug_t = threading.Thread(target=self.debug_disp)
        debug_t.start()

    """ Init display vars for new question / entering room """
    def init_disp(self):
        # Determines time passed
        time_passed = (self.pb.data['real_time'] - self.pb.data['time_offset'] - self.pb.data['begin_time'])

        if self.pb.game_state == GameState.BUZZED:
            time_passed = (self.pb.data['time_freeze'] - self.pb.data['begin_time'])

        # Calculates current index and display
        accum = 0
        qList = self.pb.data['question'].split(' ')
        for i in range(len(self.pb.data['timing'])):
            self.local_index = i
            self.disp += qList[i] + ' '
            accum += round(self.pb.data['timing'][i]*self.pb.data['rate'])

            if accum >= time_passed:
                break

        self.local_time = self.pb.data['real_time']

    """ Runs client to display """
    def update_disp(self):
        while True:
            # Update display if detect a new question
            if self.pb.game_state == GameState.NEW_Q:
                self.pb.game_state = GameState.RUNNING
                self.init_disp()

            # Run client-side display update
            try:
                if self.pb.game_state == GameState.RUNNING:
                    if self.local_index < len(self.pb.data['timing']):
                        qList = self.pb.data['question'].split(' ')

                        self.disp = ' '.join(qList[:self.local_index])

                        current_interval = round(self.pb.data['timing'][self.local_index]*self.pb.data['rate'])
                        time.sleep(current_interval / 1000)
                        self.local_time += current_interval
                        self.local_index += 1

                    else:
                        # Add way to differentiate reading end and question end?
                        self.pb.game_state = GameState.IDLE

                # Auto fill if question ends
                if self.pb.game_state == GameState.IDLE:
                    self.disp = self.pb.data['question']

            except KeyError:
                print('error')

    """ Debug display """
    def debug_disp(self):
        while True:
            print('======================================')
            print(self.local_index)
            print(self.disp)
            print('--------------------------------------\n')
