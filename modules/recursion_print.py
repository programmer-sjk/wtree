import os
from modules.constants import CONNECT_CHAR, CONNECT_CHAR_MORE, CONNECT_CHAR_END, CONNECT_CHAR_ROOT
dir_count = 0

def print_items(args, last_dir_idx, depth = 1):    
    print_files, print_dirs = _get_print_closures(args, last_dir_idx, depth)

    if args['opt'] == '-d':
        #print_files = None
        pass
    elif args['opt'] == '-f':
        #print_files = None
        pass
    elif args['opt'] == '-L':
        pass

    #print_files()
    print_dirs()

def _get_print_closures(args, last_dir_idx, depth):
    (space, dspace) = (' ', '  ')
    root_char = connect_char = ''

    path = args['path']
    files, dirs = _get_files_and_directories(path)

    def _print_file_format():
        global dir_count
        for idx, name in enumerate(files):
            if depth == 1:
                (root_char, connect_char) = (CONNECT_CHAR_MORE, CONNECT_CHAR * depth)
            elif dir_count == last_dir_idx:
                if len(files) == 1 or idx + 1== len(files):
                    (root_char, connect_char) = (space, dspace * depth + CONNECT_CHAR_END)
                else:
                    (root_char, connect_char) = (space, dspace * depth + CONNECT_CHAR_MORE)
            elif idx == 0:
                if len(files) == 1:
                    (root_char, connect_char) = (CONNECT_CHAR_ROOT, dspace * depth + CONNECT_CHAR_END)
                else:
                    (root_char, connect_char) = (CONNECT_CHAR_ROOT, dspace * depth + CONNECT_CHAR_MORE)
            elif len(dirs) == 0 and idx + 1== len(files):
                (root_char, connect_char) = (CONNECT_CHAR_ROOT, dspace * depth + CONNECT_CHAR_END)
            else:
                (root_char, connect_char) = (CONNECT_CHAR_ROOT, dspace * depth + CONNECT_CHAR_MORE)
            print(root_char + connect_char + name)

    def _print_dir_format():
        global dir_count
        for idx, name in enumerate(dirs):
            if depth == 1:
                if idx + 1 == last_dir_idx:
                    (root_char, connect_char) = (CONNECT_CHAR_END, CONNECT_CHAR * depth)
                else:
                    (root_char, connect_char) = (CONNECT_CHAR_MORE, CONNECT_CHAR * depth)    
                dir_count = dir_count + 1
            elif idx == 0:
                (root_char, connect_char) = (CONNECT_CHAR_ROOT, dspace * depth + CONNECT_CHAR_END)    
            else:
                (root_char, connect_char) = (CONNECT_CHAR_MORE, CONNECT_CHAR * depth)

            _print_blue(root_char + connect_char, name)

            args['path'] = path + '/' + name
            print_items(args, last_dir_idx, depth + 1)

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

def _print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)   