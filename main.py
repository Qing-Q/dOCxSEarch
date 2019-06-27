#!/usr/bin/env python3
#coding:utf-8

from lib import print_
from lib import red
from lib import blue
from lib import green
from lib.arGParse import _argparse
from src.dOcxSEarch import seARch

# test
args = _argparse()


def main():
    path = args.path
    search = seARch(path)
    search.seArch()
    



if __name__ == "__main__":
    main()

