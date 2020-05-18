import os
from modules.constants import CONNECT_CHAR, CONNECT_CHAR_MORE, CONNECT_CHAR_END, CONNECT_CHAR_ROOT
dir_count = 0




def recursive_print(path, last_dir_idx, depth = 1):
    global dir_count
    (space, dspace) = (' ', '  ')
    (files, dirs) = ([], [])
    root_char = connect_char = ''
    

    with os.scandir(path) as entries:
        for idx, entry in enumerate(entries):
            if entry.is_file():
                files.append(entry.name)
            if entry.is_dir():
                dirs.append(entry.name)

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
            
        
        print_blue(root_char + connect_char, name)
        depth = depth + 1
        recursive_print(path + '/' + name, last_dir_idx, depth)
        depth = depth - 1

def print_blue(plain, dirname):
    (BLUE_COLOR, END_COLOR) = ('\033[94m', '\033[0m')
    print(plain + BLUE_COLOR + dirname + END_COLOR)   