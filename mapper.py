#!/usr/bin/python
import sys
import os
filter1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
filter2 = ['Media'.lower(), 'Special'.lower(), 'Talk'.lower(), 'User'.lower(), 'User_talk'.lower(), 'Project'.lower(), 'Project_talk'.lower(), 'File'.lower(), 'File_talk'.lower(), 'MediaWiki'.lower(), 'MediaWiki_talk'.lower(), 'Template'.lower(), 'Template_talk'.lower(), 'Help'.lower(), 'Help_talk'.lower(), 'Category'.lower(), 'Category_talk'.lower(), 'Portal'.lower(), 'Wikipedia'.lower(), 'Wikipedia_talk'.lower()]
filter3 = ['.jpg', '.gif', '.png', '.JPG', '.GIF', '.PNG', '.txt', '.ico']
filter4 = ['404_error/', 'Main_Page', 'Hypertext_Transfer_Protocol', 'Search']
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    file_name = os.environ["mapreduce_map_input_file"]
    date = file_name.split('/', 2)[2].split('-', 3)[1]
    date = date[0:len(date)-3]+"-"+date[len(date)-2:]
    if not any(elem == '' or elem is None for elem in words):
        if words[0]=='en':
            if (words[1][:1] not in filter1):
                title = words[1].split(":", 1)[0].lower()
                if title.lower() not in filter2:
                    if words[1][-4:] not in filter3:
                        if title not in filter4:
                            print('{:s}\t{:s}\t{:s}'.format(words[1], words[2], date))


