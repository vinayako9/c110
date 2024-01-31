#import the time module

import time

#impout time in sec

seconds=input("enter seconds : ")

#def contoun timer for mins

def countdown_timer(seconds):

    while seconds > 0:

      mins=int(seconds / 60)
      secs=int(seconds % 60)

      timer = f'{mins}:{secs}'

      print(timer)

      seconds -=1

    print('Time Up!')  

#function call
countdown_timer(int(seconds))    