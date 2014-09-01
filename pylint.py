#!/usr/bin/python

from subprocess import check_call
from sys import argv

if __name__ == '__main__':
    check_call('pylint {}'.format(argv[1]))
