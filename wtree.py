import os
import sys
from modules.arguments import *
from modules.recursion_print import print_items
arg_len = len(sys.argv)

def get_last_dir_index(path):
    with os.scandir(path) as entries:
        return sum(1 for e in entries if e.is_dir())

if is_args_valid(arg_len):
    args = parse_args(arg_len)
    if is_each_value_valid(args):
        print(args['path'])
        
        args['path'] = "C:\\Users\\Mement\\Desktop\\side_project\\study\\principle" #os.getcwd()
        last_dir_idx = get_last_dir_index(args['path'])
        print_items(args, last_dir_idx)
    else:
        print_usage()
        
    
    
    
