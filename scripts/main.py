#!/usr/bin/env python3
import os, sys, shutil
import argparse

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


def recite_zen_of_python(*args, **kwargs):
    import this

def has_git_repo(path="."):
    """
    Checks whether the provided directory is a git repository

    Keyword arguments:
    path -- a directory (default ".")

    Return: boolean
    """
    return ".git" in os.listdir(path)

def main(args):
    print("hello git!")
    for path in args.paths:
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
        
if __name__ == '__main__':
    # ---- Setup CLI argument parser
    main_parser = argparse.ArgumentParser("git-cc", description='Ma thèse en 180 commits')
    subparsers = main_parser.add_subparsers(help='sub-command help')

    # Zen reciter module
    zen_parser = subparsers.add_parser("zen", help='zen help')
    zen_parser.set_defaults(func=recite_zen_of_python)
    # Git finder module 
    git_parser = subparsers.add_parser("git-finder", help='git-finder help')
    git_parser.add_argument("paths", default=["."], nargs=argparse.REMAINDER)
    git_parser.set_defaults(func=main)
    # ---- Parse arguments
    args = main_parser.parse_args()

    try:
        args.func(args)
        sep_line()
        print("Done!")
    except KeyboardInterrupt:
        print('User has exited the program')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

