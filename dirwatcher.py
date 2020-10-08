#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Jalal"


import argparse
import sys


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    """Create a command line parser and setup cmd line arguments."""
    parser = argparse.ArgumentParser(
        description="Check the directory for a magic word")
    parser.add_argument(
        '-e', help='extension of file name', default=".txt")
    parser.add_argument(
        '-i', help='--interval', default=1)
    parser.add_argument(
        'magic', help='magic word to find')
    parser.add_argument(
        '-d', '--dir', default='.', help="directory to watch, defaults to '.'")
    return parser


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
