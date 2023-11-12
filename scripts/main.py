#!/usr/bin/env python3
import os, sys, shutil, inspect
import argparse

def get_shell_width():
    return shutil.get_terminal_size().columns

def sep_line(width=None, sep='─', file=sys.stdout):
    """
    Print a separatory line spanning the whole shell's width

    Keyword arguments:
    size -- width of the separatory line (default: None)
    sep  -- character used to build the separatory line (default: U+2500)
    file -- ioctl device where the line should be printed (default: sys.stdout)

    Return: None
    """
    width = get_shell_width() if width is None else width
    print(sep * width, file=file)


def get_function_name(stack_index=1, func=None):
    return inspect.stack()[stack_index].function if func is None else func.__name__

def print_module_header(func=None):
    module_name=get_function_name(stack_index=2, func=func).replace("_", "-")
    print(f"Running module '{module_name}'".center(get_shell_width()))
    sep_line()


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

def hello(*args, **kwargs):
    print("hello git!")

def git_finder(args):
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

    # Hello module
    hello_parser = subparsers.add_parser("hello", help="hello help")
    hello_parser.set_defaults(func=hello)
    # Zen reciter module
    zen_parser = subparsers.add_parser("zen", help='zen help')
    zen_parser.set_defaults(func=recite_zen_of_python)
    # Git finder module 
    git_parser = subparsers.add_parser("git-finder", help='git-finder help')
    git_parser.add_argument("paths", default=["."], nargs=argparse.REMAINDER)
    git_parser.set_defaults(func=git_finder)
    # ---- Parse arguments
    args = main_parser.parse_args()

    # ---- Print usage if no arguments provided
    if len(sys.argv)==1:
        main_parser.print_help(file=sys.stderr)
        sys.exit(1)

    # ---- Main
    try:
        print_module_header(args.func)
        args.func(args)
        sep_line()
        print("Done!")
    except KeyboardInterrupt:
        print('User has exited the program')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

