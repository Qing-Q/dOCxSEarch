# -*- coding:utf-8 -*-
import sys
import docx

path = sys.argv[1]

file = docx.Document(path)
for para in file.paragraphs:
	print para.text





    