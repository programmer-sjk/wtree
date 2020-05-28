import sys
from .constants import valid_opts

def is_args_valid(arg_len):
    if _is_len_valid(arg_len):
        return True
        
    print_usage()
    return False

_is_len_valid = lambda arg_len: arg_len < 5

def print_usage(): # 기능 개발 후 최종 추가
    print("""usage: python wtree.py [path] [option]
    path  Description
    - if you dont give path argument, wtree search files and directory from current path
    - you can give specific path to argument,          ex) python wtree.py modules
    - you can give currnet directory path to argument, ex) python wtree.py .
    options Description
    -d: search only directory from path
    -f: search only file from path
    -L: search given depth sub dir.
        ex) python wtree.py -L 2  - it finds file and directory in 2 depth directory from current directory
    """)

def parse_args(arg_len):
    args = {"path": None, "opt": None, "extra": None}

    if arg_len == 1:
        args['path'] = "."
    else:
        args['path'], args['opt'], args['extra'] = _parse_args(arg_len)
    return args

def _parse_args(arg_len):

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

def is_each_value_valid(args):
    path, opt, extra = args['path'], args['opt'], args['extra']
    if _path_check(path) and _opt_check(opt) and _extra_check(opt, extra):
        return True
    return False
    
def _path_check(path):
    if path == '.' or isinstance(path, str):
        return True
    return False

def _opt_check(opt):
    if opt == None or opt in valid_opts:
        return True
    return False

def _extra_check(opt, extra):
    try:
        if (opt != '-L' and extra == None) or (opt == '-L' and int(extra)):
            return True
    except:
        return False
    return False