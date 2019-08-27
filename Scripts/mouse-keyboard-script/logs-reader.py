def clear_file(name):
    open(name, 'w').close()


def count_lines(name):
    file = open(name)
    count = len(file.readlines())
    print(count)
    file.close()

mouse_file = "/home/abc/Downloads/mouse_log.txt"

keyboard_file = "/home/abc/Downloads/keyboard_log.txt"
count_lines(mouse_file)
clear_file(mouse_file)
count_lines(keyboard_file)
clear_file(keyboard_file)