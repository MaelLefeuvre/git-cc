#!/usr/bin/env python3
import sys
import shutil


def sep_line(width=None, sep='─', file=sys.stdout):
    """
    Print a separatory line spanning the whole shell's width

    Keyword arguments:
    size -- width of the separatory line (default: None)
    sep  -- character used to build the separatory line (default: U+2500)
    file -- ioctl device where the line should be printed (default: sys.stdout)

    Return: None
    """
    width = shutil.get_terminal_size().columns if width is None else width
    print(sep * width, file=file)


def recite_zen_of_python():
    import this

def main():
    print("hello git!")
    sep_line()
    recite_zen_of_python()

if __name__ == '__main__':
    main()
