#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import os
import sys

#########################################################
# Functions
#########################################################


def getPath(__file__):
    return os.path.abspath(os.path.dirname(__file__))


def getRoot():
    return sys.path[1]


def getSpecificParentDir(__file__, dirName):
    pth = getPath(__file__)
    pth = (pth.split(dirName)[0]+'\\'+dirName).replace('\\\\', '\\')
    return pth


def getRootByName(__file__, dirName):
    return getSpecificParentDir(__file__, dirName)


def getSpecificChildDir(__file__, dirName):
    pth = getPath(__file__)
    for x in [x[0] for x in os.walk(pth)]:
        if dirName in x:  # Needs improvement cause of different cases
            return (pth.split(dirName)[0]+'\\'+dirName).replace('\\\\', '\\')
    return None  # Not found


print(getRoot())
print(getRootByName(__file__, 'PyHelper'))
print(getSpecificParentDir(__file__, 'PyHelper'))
print(getSpecificParentDir(__file__, 'scripts'))
print(getSpecificChildDir(__file__, 'sub1'))
