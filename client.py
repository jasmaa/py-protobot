from protobowl import GameState
import time
import threading

""" Class for tracking and syncing questions """
class Client:

    def __init__(self, pb):
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

        if self.pb.game_state == GameState.RUNNING:
            time_passed = (self.pb.data['real_time'] - self.pb.data['time_offset'] - self.pb.data['begin_time'])
        elif self.pb.game_state == GameState.BUZZED:
            time_passed = (self.pb.data['time_freeze'] - self.pb.data['begin_time'])

        accum = 0
        disp = ''
        qList = self.pb.data['question'].split(' ')

        for i in range(len(self.pb.data['timing'])):
            self.local_index = i
            disp += qList[i] + ' '
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
                        current_interval = round(self.pb.data['timing'][self.local_index]*self.pb.data['rate'])
                        time.sleep(current_interval / 1000)
                        self.local_time += current_interval
                        self.local_index += 1

                        self.disp = ' '.join(qList[:self.local_index])

                    else:
                        print('question end')
                        time.sleep(self.pb.data['answer_duration'] / 1000)
                        self.pb.game_state = GameState.IDLE
                        print('booyah')
            except KeyError:
                print('error')


    """ Debug display """
    def debug_disp(self):
        while True:
            print('======================================')
            print(self.local_index)
            print(self.disp)
            print('--------------------------------------\n')
