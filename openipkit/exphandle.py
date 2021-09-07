#########################################################
# Author: sh-navid
#########################################################
'''
'''
#########################################################
# Add preprocessors
#########################################################
DEFINE_BACKEND = '''
    Hello :)
    this module is depends on a few modules.
    you should define a backend for your project.

    after importing backend; do this:

    import scripts.backend as back
    back.backend_engine=ANY_IMAGE_ENGINE_YOU_WANT
'''

ECHO_TYPE_WARNING = 0


def echo(txt, echoType=ECHO_TYPE_WARNING):
    print('\n', "#"*80)
    if echoType == ECHO_TYPE_WARNING:
        print("...WARNING...")
    print(txt)
    print("#"*80)
