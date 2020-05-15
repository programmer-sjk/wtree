import os
import sys
from modules.arguments import *
arg_len = len(sys.argv)


if is_args_valid(arg_len):
    args = parse_args(arg_len)
    if is_each_value_valid(args):
        current_path = "C:\\Users\\MEMENT\\Desktop\\side_project\\study\\principle" #os.getcwd()
        """
        for path, dirs, files in os.walk(current_path):
            print(path.split(os.path.sep)[-1])
            print(dirs)
            print(path)
            
            print(files)
            print('===')
        """
        with os.scandir(current_path) as entries:
            for entry in entries:
                print(entry.name)
            
            for entry in entries:
                if entry.is_file():
                    print('file:' + entry.name)
                if entry.is_dir():
                    print('dir:' + entry.name)
        
    else:
        print_usage()
        
    
    
    
