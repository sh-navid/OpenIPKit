#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
from datetime import datetime


def execMonitor(func, printTime=True):
    t1 = datetime.now()
    func()
    t2 = datetime.now()
    t2 = t2-t1
    if printTime:
        print(f"Exec time of({type(func)}): {str(t2)}")
    return t2
