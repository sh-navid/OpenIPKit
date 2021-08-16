#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
import os
from posixpath import dirname
import sys

#########################################################
# Functions
#########################################################

TEMP_DELIMITER = '|'
PATH_DELIMITER='\\'


def cleanPath(pth):
    pth = pth.replace('/', TEMP_DELIMITER)
    pth = pth.replace('\\', TEMP_DELIMITER)
    return pth


def listPath():
    return sys.path


def getPath(__file__):
    return os.path.abspath(os.path.dirname(__file__))


def getRootByName(__file__, dirName):
    return getSpecificParentDir(__file__, dirName)


def getSpecificParentDir(__file__, dirName):
    pth = cleanPath(getPath(__file__))
    dirName = cleanPath(dirName)
    candidate = f'{TEMP_DELIMITER}{dirName}{TEMP_DELIMITER}'
    if candidate in pth:
        pth = (pth.split(candidate)[0]+TEMP_DELIMITER +
               dirName).replace(TEMP_DELIMITER+TEMP_DELIMITER, TEMP_DELIMITER)
        pth=pth.replace(TEMP_DELIMITER,PATH_DELIMITER)
        return pth
    return None


def getSpecificChildDir(__file__, dirName):
    pth = getPath(__file__)
    for x in [x[0] for x in os.walk(pth)]:
        if dirName in x:  # Needs improvement cause of different cases
            return (pth.split(dirName)[0]+'\\'+dirName).replace('\\\\', '\\')
    return None  # In case not found


# print('\n\n\n')
# print(listPath())
print('\ngetPath:              ', getPath(__file__))
print('\ngetRootByName:        ', getRootByName(__file__, 'PyHelper'))
print('\ngetSpecificParentDir: ', getSpecificParentDir(__file__, 'PyHelper'))
print('\ngetSpecificParentDir: ', getSpecificParentDir(__file__, 'scripts'))
print('\ngetSpecificChildDir:  ', getSpecificChildDir(__file__, 'sub1'))
