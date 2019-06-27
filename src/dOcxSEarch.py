#!/usr/bin/env python3
#coding:utf-8


import docx


class seARch(object):

    def __init__(self,path):
        self.fiLe = docx.Document(path)

    def seArch(self):
        for para in self.fiLe:
            print(para.text)
    


