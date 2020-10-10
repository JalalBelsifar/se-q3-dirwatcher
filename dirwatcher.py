#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "jalal"

import sys
import argparse
import os

tracking_dict = {}


def search_for_magic(magic_string, line, file_title, line_index, path):
    """Searches a read line for a magic word and
     only logs when magic word is found ."""
    if magic_string in line:
        (
            f'Magic text found: line {line_index + 1} of file '
            f'{os.path.join(path, file_title)}')


def scan_single_file(tracking_dict, extension, path, magic_string):
    """Return a file with the proper extension"""
    for file_title in tracking_dict:
        with open(os.path.join(path, file_title)) as read_f:
            line_index = tracking_dict[file_title]
            lines = read_f.readlines()[line_index:]
            for line in lines:
                search_for_magic(magic_string, line,
                                 file_title, line_index, path)
                line_index += 1
                tracking_dict.update({file_title: line_index})


def check_added_files(path, new_file_dict, tracking_dict):
    """Return a list of newly added files and adds them to global dict."""


def check_deleted_files(path, new_file_dict):
    """Logs removed files from provided directory and
    adds them to global dict."""


def watch_directory(path, magic_string, extension, interval):
    print(path, magic_string, extension, interval)
    return


def create_parser():
    """Creates parser and setup cmd line options."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-dir', '--directory', default='.',
                        help='Directory to be watched.')
    parser.add_argument('-ext', '--extension', default='txt',
                        help='Extentions to be watched.')
    parser.add_argument('-int', '--interval', type=int, default=1,
                        help='Polling interval. Default 1.0 seconds')
    parser.add_argument('magic', help='Magic word to be found')
    return parser


def signal_handler(sig_num, frame):
    """Signal Handler for SIGTERM and SIGINT."""


def main(args):
    """Create a command line parser for dirwatcher."""

    parser = create_parser()
    ns = parser.parse_args(args)
    print(ns)

    if not ns:
        parser.print_usage(args)
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
