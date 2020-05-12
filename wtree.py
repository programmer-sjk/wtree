import os
import sys

arg_len = len(sys.argv)

def is_valid():
    if(arg_len > 2):
        print_usage()
        return False
    return True

def print_usage():
    print("usage: ")

def init():
    option = ''
    if(arg_len > 1):
        option = getOption()
    return option

        
def getOption():
    return {
        "-L": "-L"
    }.get(sys.argv[1])

if(is_valid()):
    option = init()
    #print(option)

    

