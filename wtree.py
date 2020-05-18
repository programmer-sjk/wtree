import os
import sys
from modules.arguments import *
from modules.recursion_print import recursive_print
arg_len = len(sys.argv)

def get_last_dir_index(path):
    with os.scandir(path) as entries:
        return sum(1 for e in entries if e.is_dir())


if is_args_valid(arg_len):
    args = parse_args(arg_len)
    if is_each_value_valid(args):
        current_path = "C:\\Users\\Mement\\Desktop\\side_project\\study\\principle" #os.getcwd()
        print(args['path'])          
        last_dir_idx = get_last_dir_index(current_path)
        recursive_print(current_path, last_dir_idx)
        
    else:
        print_usage()
        
    
    
    
