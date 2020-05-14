import os
import sys

arg_len = len(sys.argv)

def is_args_valid():
    if _is_len_valid():
        return True
        
    print_usage()
    return False

_is_len_valid = lambda: arg_len < 5

def parse_args():
    args = {"path": None, "opt": None, "extra": None}

    if arg_len == 1:
        args['path'] = "."
    else:
        args['path'], args['opt'], args['extra'] = _parse_args()
    return args

def _parse_args():

    path = "."
    opt = None
    extra = None

    if arg_len == 2:  
        if '-' in sys.argv[1]:
            opt = sys.argv[1]
        else:
            path = sys.argv[1]

    elif arg_len == 3:
        if '-' in sys.argv[1]:
            if 'L' in sys.argv[1]:
                opt = '-L'
                extra = sys.argv[2]
            else:
                opt = sys.argv[1]
                path = sys.argv[2]
        else:
            path = sys.argv[1]
            opt = sys.argv[2]

    elif arg_len == 4:
        if '-L' == sys.argv[1]:
            opt = '-L'
            extra = sys.argv[2]
            path = sys.argv[3]
        else:
            opt = '-L'
            extra = sys.argv[3]
            path = sys.argv[1]

    return path, opt, extra

def print_usage(): # 기능 개발 후 최종 추가
    print("usage: ")

if is_args_valid():
    args = parse_args()
    print(args)
    sys.exit() 
    
    current_path = "C:\\Users\\MEMENT\\Desktop\\side_project\\study\\principle" #os.getcwd()
    """
    with os.scandir(current_path) as entries:
        for entry in entries:
            print(entry.name)
        
        for entry in entries:
            if entry.is_file():
                print('file:' + entry.name)
            if entry.is_dir():
                print('dir:' + entry.name)
        
    
    for path, dirs, files in os.walk(current_path):
        print(dirs)
        print(path)
        
        #print(files)
        print('===')
    """
    
