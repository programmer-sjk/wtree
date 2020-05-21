import os
from modules.constants import HORIZEN_CHAR, VERTICAL_CHAR, CONNECT_CHAR, END_CHAR
dir_count = 0

def print_items(args, last_dir_idx, depth = 1, parent_dir_is_last = False):    

    if args['opt'] == '-L':
        if depth > int(args['extra']):
            return None

    print_files, print_dirs = _get_print_closures(args, last_dir_idx, depth)

    file_flag = dir_flag = None

    if args['opt'] == '-d':
        dir_flag = True
    elif args['opt'] == '-f':
        file_flag = True
    else:
        file_flag = dir_flag = True

    if file_flag:
        print_files()

    if dir_flag:
        print_dirs(parent_dir_is_last)

def _get_print_closures(args, last_dir_idx, depth):
    (space, dspace) = (' ', '  ')
    root_char = connect_char = ''

    path = args['path']
    files, dirs = _get_files_and_directories(path)

    def _print_file_format():
        global dir_count
        for idx, name in enumerate(files):
            if depth == 1:
                (root_char, connect_char) = (CONNECT_CHAR, HORIZEN_CHAR* depth)
            elif dir_count == last_dir_idx:
                if len(files) == 1 or idx + 1== len(files):
                    (root_char, connect_char) = (space, dspace * depth + END_CHAR)
                else:
                    (root_char, connect_char) = (space, dspace * depth + CONNECT_CHAR)
            elif idx == 0:
                if len(files) == 1:
                    (root_char, connect_char) = (VERTICAL_CHAR, dspace * depth + END_CHAR)
                else:
                    (root_char, connect_char) = (VERTICAL_CHAR, dspace * depth + CONNECT_CHAR)
            elif len(dirs) == 0 and idx + 1== len(files):
                (root_char, connect_char) = (VERTICAL_CHAR, dspace * depth + END_CHAR)
            else:
                (root_char, connect_char) = (VERTICAL_CHAR, dspace * depth + CONNECT_CHAR)
            print(root_char + connect_char + name)

    def _print_dir_format(parent_dir_is_last):
        global dir_count
        for idx, name in enumerate(dirs):
            if depth == 1:
                if idx + 1 == last_dir_idx:
                    root_char = END_CHAR
                else:
                    root_char = CONNECT_CHAR

                connect_char = _get_connect_char(depth, False)
                dir_count = dir_count + 1
            else:
                root_char = VERTICAL_CHAR
                connect_char = _get_connect_char(depth, parent_dir_is_last)

                if idx + 1 == len(dirs):
                    connect_char = connect_char + END_CHAR
                else:
                    connect_char = connect_char + CONNECT_CHAR                
             
            _print_blue(root_char + connect_char, name)

            args['path'] = path + '/' + name
            print_items(args, last_dir_idx, depth + 1, idx + 1 == len(dirs))

    return _print_file_format, _print_dir_format

def _get_files_and_directories(path):
    files, dirs = ([] for i in range(2))

    with os.scandir(path) as entries:
        for idx, entry in enumerate(entries):
            if entry.is_file():
                files.append(entry.name)
            if entry.is_dir():
                dirs.append(entry.name)
    return files, dirs

def _get_connect_char(depth, parent_dir_is_last):
    if depth == 1:
        return HORIZEN_CHAR* depth
    else:
        return _make_connect_char(depth, parent_dir_is_last)

def _make_connect_char(depth, parent_dir_is_last):
    ret = dspace = '  '
    
    count = parent_dir_is_last and depth - 3 or depth - 2
    for _ in range(count): 
        ret = ret + '│' + dspace
    
    if parent_dir_is_last: 
        ret = ret + dspace    
    
    return ret

def _print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)   