#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import sys
sys.path.append('.')
import openipkit.nssys as nss
import openipkit.nsproc as proc
import openipkit.nsdraw as draw
import openipkit.nscolor as nsc
import openipkit.backend as back
import openipkit.ml.nslearn as learn

#########################################################
# Source code
#########################################################
im = back.imread(sys.path[0]+'/media/im.png')

def run():
    global im
    im = draw.grid(im)
    im = draw.grid(im, color1=(127,0,255),color2=(200,200,200),thickness=20)
    print(signature(draw.grid))

nss.execMonitor(run,True)
back.imshow('Test', im)