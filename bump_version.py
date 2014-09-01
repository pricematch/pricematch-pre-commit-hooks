#!/usr/bin/python

from subprocess import check_call
from sys import argv


def bump_version(path):
    with open(path, 'r') as f:
        new_version = 1 + int(f.read())
    with open(path, 'w') as f:
        f.write(str(new_version))
    check_call('git add assets/VERSION')


if __name__ == '__main__':
    bump_version(argv[1])
