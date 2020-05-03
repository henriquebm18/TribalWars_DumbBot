
import time
import webbrowser
from sys import platform
from random import random

import pyautogui
#run from terminal in a virtual machine

#%% parametres a modifier

villages_code = [25599, 28334, 23820]
#how_many_barbers = [55, 100, 180]
how_many_barbers = [25, 50, 50]
time_space = 60 #minutes

#%%
class KeyboardCommands():
    def run_js_script(self):
        pyautogui.press('9')

    def close_tab(self):
        if platform == 'darwin':
            pyautogui.keyDown('cmd')  # hold down the shift key
            pyautogui.press('w')     # press the left arrow key
            pyautogui.keyUp('cmd')    # release the shift key
        else:
            pyautogui.keyDown('ctrl')  # hold down the shift key
            pyautogui.press('w')     # press the left arrow key
            pyautogui.keyUp('ctrl')    # release the shift key

    def send_spaced_bs(self, how_much):
        for x in range(how_much):
            pyautogui.press('b')
            time.sleep(.2+random()/10)

    def send_spaced_2bs(self, how_much):
        for x in range(how_much):
            pyautogui.press('b')
            time.sleep(.2+random()/10)

    def send_spaced_as(self, how_much):
        for x in range(how_much):
            pyautogui.press('a')
            time.sleep(.2+random()/10)

def open_farm_tab(village):
    if platform == 'darwin':
        webbrowser.get('Chrome').open('https://br100.tribalwars.com.br/game.php?village={}&screen=am_farm'.format(village), new=2, autoraise=True)
    elif platform == 'linux':
        webbrowser.get('Firefox').open('https://br100.tribalwars.com.br/game.php?village={}&screen=am_farm'.format(village), new=2, autoraise=True)
    else:
        webbrowser.open('https://br100.tribalwars.com.br/game.php?village={}&screen=am_farm'.format(village), new=2, autoraise=True)

def farm_coordinator(tcl):
    ##
    for x in range(len(villages_code)):
        # print(x, villages_code[x])
        open_farm_tab(villages_code[x])
        time.sleep(5)
        tcl.run_js_script()
        time.sleep(4)
        tcl.send_spaced_as(12)
        tcl.send_spaced_bs(how_many_barbers[x])
        time.sleep(.5)
        tcl.close_tab()
#%%
if __name__ == '__main__':
    tcl = KeyboardCommands()

    try:
        while True:
            #for x in range(3):
            #    print('\r\a', end='', flush=True)
            #    time.sleep(1)
            print(time.strftime("%a, %d %b %Y %H:%M:%S"))
            s = time.time()
            farm_coordinator(tcl)
            elapsed_time = time.time()-s
            print('done in {}s\n.'.format(round(elapsed_time,3)))
            time.sleep(60*(time_space-elapsed_time/60))
    except KeyboardInterrupt:
           print('\n')
