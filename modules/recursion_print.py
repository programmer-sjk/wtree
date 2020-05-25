import os
import copy
import colorama
from modules.constants import HORIZEN_CHAR, VERTICAL_CHAR, CONNECT_CHAR, END_CHAR
dir_count = 0

colorama.init()

def print_items(args, last_dir_idx, depth = 1, parents_last_infoes = [False]):    

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
        print_files(parents_last_infoes)

    if dir_flag:
        print_dirs(parents_last_infoes)

def _get_print_closures(args, last_dir_idx, depth):
    (space, dspace) = (' ', '  ')
    root_char = connect_char = ''

    path = args['path']
    files, dirs = _get_files_and_directories(path)

    def _print_file_format(parents_last_infoes):
        global dir_count
        for idx, name in enumerate(files):
            root_char = _get_root_char(idx)
            connect_char = _get_connect_char(idx, parents_last_infoes, len(files) + len(dirs))
            print(root_char + connect_char + ' ' + name)

    def _print_dir_format(parents_last_infoes):
        for idx, name in enumerate(dirs):

            root_char = _get_root_char(idx)
            connect_char = _get_connect_char(idx, parents_last_infoes, len(dirs))

            _print_blue(root_char + connect_char, name)

            args['path'] = path + '/' + name
            temp = copy.deepcopy(parents_last_infoes)
            temp.append(idx + 1 == len(dirs))
            print_items(args, last_dir_idx, depth + 1, temp)

    def _get_root_char(index):
        global dir_count
        if depth == 1:
            if _is_last_directory(index, last_dir_idx):
                root_char = END_CHAR
            else:
                root_char = CONNECT_CHAR
            dir_count = dir_count + 1
        elif last_dir_idx == dir_count:
            root_char = '' 
        else:
            root_char = VERTICAL_CHAR
        return root_char

    def _get_connect_char(index, parents_last_infoes, length):
        if depth == 1:
            return HORIZEN_CHAR * depth
        else:
            connect_char = _make_connect_char(parents_last_infoes)
            if _is_last_directory(index, length):
                return connect_char + END_CHAR
            else:
                return connect_char + CONNECT_CHAR
            
    def _make_connect_char(parents_last_infoes):
        ret = dspace = '  '
        count = depth - 2

        if depth > 2:
            for parent_info in parents_last_infoes[2:]:
                if not parent_info:
                    ret = ret + VERTICAL_CHAR + dspace #+ str(parent_info)
                else:
                    ret = ret + dspace #+ str(parent_info)

        return ret

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

def _is_last_directory(index, dir_all_count):
    return index + 1 == dir_all_count

def _print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)   