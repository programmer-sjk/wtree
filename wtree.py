import os
import sys
from modules.arguments import *
arg_len = len(sys.argv)

CONNECT_CHAR = '──'
CONNECT_CHAR_MORE = '├─'
END_CONNECT_CHAR = '└─'
ROOT_VERTI_LINE = '│'

def rescursive_print(path, depth = 1, is_last = False):
    indent = '  '
    files = []
    dirs = []

    with os.scandir(path) as entries:
        total_length = sum(1 for e in entries)

    with os.scandir(path) as entries:
        for idx, entry in enumerate(entries):
            if entry.is_file():
                files.append(entry.name)
            if entry.is_dir():
                dirs.append(entry.name)

    for idx, name in enumerate(files):
        if depth == 1:
            print(CONNECT_CHAR_MORE + CONNECT_CHAR * depth + name)
        elif idx == 0:
            if len(files) == 1:
                print(ROOT_VERTI_LINE + indent * depth + END_CONNECT_CHAR + name)
            else:
                print(ROOT_VERTI_LINE + indent * depth + CONNECT_CHAR_MORE + name)
        elif len(dirs) == 0 and idx + 1== len(files):
            print(ROOT_VERTI_LINE + indent * depth + END_CONNECT_CHAR + name)
        else:
            print(ROOT_VERTI_LINE + indent * depth + CONNECT_CHAR_MORE + name)
                
    for idx, name in enumerate(dirs):
        if depth == 1:
            print_blue(CONNECT_CHAR_MORE + CONNECT_CHAR * depth, name)
        elif idx == 0:
            print_blue(ROOT_VERTI_LINE + indent * depth + END_CONNECT_CHAR, name)
        else:
            print_blue(CONNECT_CHAR_MORE + CONNECT_CHAR * depth , name)         
        
        depth = depth + 1
        print(idx + 1 == len(dirs), name)
        rescursive_print(path + '/' + name, depth, idx + 1 == len(dirs))
        depth = depth - 1

def print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)        

if is_args_valid(arg_len):
    args = parse_args(arg_len)
    if is_each_value_valid(args):
        current_path = "C:\\Users\\MEMENT\\Desktop\\side_project\\study\\principle" #os.getcwd()
        print(args['path'])          
        
        rescursive_print(current_path)
        
    else:
        print_usage()
        
    
    
    
