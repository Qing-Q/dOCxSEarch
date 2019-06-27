#!/usr/bin/env python3
#coding:utf-8









W = '\033[0m'

G = '\033[1;32m'
O = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'


def print_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    print(color+content+W)


def red(content):
    print(R+content+W)

def greed(content):
    print(G+content+W)

def blue(content):
    print(B+content+W)