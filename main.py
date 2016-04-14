#!/usr/bin/env python
# encoding: utf-8
# add
# from ieee import get_abstract_ieee
from springer import get_abstract_springer
# from acm import get_abstract_acm


file_content = ''
file_name_proceedings = '1023.txt'
f = open(file_name_proceedings,'r')
line = f.readline()

# f2 = open('other_urls.txt','a')

while line:
    print line.strip()
    if line == '\n':
        line = f.readline()
        continue
    url = line.strip()
    get_abstract_springer(url)
    line = f.readline()
f.close()
# f2.close()