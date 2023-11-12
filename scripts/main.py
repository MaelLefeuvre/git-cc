#!/usr/bin/env python3
import os
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

def has_git_repo(path="."):
    """
    Checks whether the provided directory is a git repository

    Keyword arguments:
    path -- a directory (default ".")

    Return: boolean
    """
    return ".git" in os.listdir(path)

def main():
    print("hello git!")
    sep_line()
    recite_zen_of_python()
    sep_line()

    for path in sys.argv[1:]:
        try:
            if has_git_repo(path):
                message = f"gitted          {path}"
            else:
                message = f"ungitted        {path}"
        except NotADirectoryError:
            message = f"not a directory {path}"
        except FileNotFoundError:
            message = f"does not exist  {path}"
        finally:
            print(message)
        
    sep_line()
    print("Done")

if __name__ == '__main__':
    main()
