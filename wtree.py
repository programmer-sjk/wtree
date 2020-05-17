import os
import sys
from modules.arguments import *
arg_len = len(sys.argv)

CONNECT_CHAR = '──'
CONNECT_CHAR_MORE = '├─'
END_CONNECT_CHAR = '└─'
ROOT_VERTI_LINE = '│'
dir_count = 0

def rescursive_print(path, last_dir_idx, depth = 1):
    global dir_count
    indent = '  '
    files = []
    dirs = []

    with os.scandir(path) as entries:
        for idx, entry in enumerate(entries):
            if entry.is_file():
                files.append(entry.name)
            if entry.is_dir():
                dirs.append(entry.name)

    for idx, name in enumerate(files):
        if depth == 1:
            print(CONNECT_CHAR_MORE + CONNECT_CHAR * depth + name)
        elif dir_count == last_dir_idx:
            if len(files) == 1 or idx + 1== len(files):
                print(' ' + indent * depth + END_CONNECT_CHAR + name)
            else:
                print(' ' + indent * depth + CONNECT_CHAR_MORE + name)
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
            if idx + 1 == last_dir_idx:
                print_blue(END_CONNECT_CHAR + CONNECT_CHAR * depth, name)
            else:    
                print_blue(CONNECT_CHAR_MORE + CONNECT_CHAR * depth, name)
            dir_count = dir_count + 1
        elif idx == 0:
            print_blue(ROOT_VERTI_LINE + indent * depth + END_CONNECT_CHAR, name)
        else:
            print_blue(CONNECT_CHAR_MORE + CONNECT_CHAR * depth , name)         
        
        depth = depth + 1
        rescursive_print(path + '/' + name, last_dir_idx, depth)
        depth = depth - 1

def print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)        

def get_last_dir_index(path):
    with os.scandir(path) as entries:
        return sum(1 for e in entries)


if is_args_valid(arg_len):
    args = parse_args(arg_len)
    if is_each_value_valid(args):
        current_path = "C:\\Users\\user\\Desktop\\side_project\\study\\principle" #os.getcwd()
        print(args['path'])          
        last_dir_idx = get_last_dir_index(current_path)
        rescursive_print(current_path, last_dir_idx)
        
    else:
        print_usage()
        
    
    
    
