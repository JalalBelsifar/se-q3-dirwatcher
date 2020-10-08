#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Jalal"


import sys
import argparse
# import os
# import signal
# import logging
# import time


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    print(path, magic_string, extension, interval)
    return


def create_parser():
    """Create a command line parser and setup cmd line arguments."""
    parser = argparse.ArgumentParser(
        description='Watches the directory for a magic word')
    parser.add_argument(
        '-e', help='extension of file name', default=".txt")
    parser.add_argument(
        '-i', help='--interval', default=1)
    parser.add_argument(
        'magic', help='magic word to find')
    parser.add_argument(
        'path', help='directory to watch')
    return parser


def signal_handler(sig_num, frame):
    print('Exiting with', sig_num)
    print('FRAME with', frame.f_lineno)
    raise SystemExit('Exiting')
    return


def main(args):
    """Implementation of dirwatcher"""
    parser = create_parser()
    ns = parser.parse_args(args)
    print(ns)

    if not ns:
        parser.print_usage(args)
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
