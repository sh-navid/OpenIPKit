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

TMP_DEL = '×'
PTH_DEL = '\\'


def cleanPath(pth):
    pth = pth.replace('/', TMP_DEL)
    pth = pth.replace('\\', TMP_DEL)
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
    candidate = f'{TMP_DEL}{dirName}{TMP_DEL}'
    if candidate in pth:
        pth = (pth.split(candidate)[0]+TMP_DEL +
               dirName).replace(TMP_DEL*2, TMP_DEL)
        return pth.replace(TMP_DEL, PTH_DEL)
    return None


def getSpecificChildDir(__file__, dirName):
    for x in [x[0] for x in os.walk(getPath(__file__))]:
        dirName = cleanPath(dirName)
        x = cleanPath(x)
        if TMP_DEL in x:
            if x.split(TMP_DEL)[-1] == dirName:
                return x.replace(TMP_DEL, PTH_DEL)
    return None


# print('\n\n\n')
# print(listPath())
print('\ngetPath:              ', getPath(__file__))
print('\ngetRootByName:        ', getRootByName(__file__, 'PyHelper'))
print('\ngetSpecificParentDir: ', getSpecificParentDir(__file__, 'PyHelper'))
print('\ngetSpecificParentDir: ', getSpecificParentDir(__file__, 'scripts'))
print('\ngetSpecificChildDir:  ', getSpecificChildDir(__file__, 'sub1'))
