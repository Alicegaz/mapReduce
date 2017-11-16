#!/usr/bin/python
import sys
current_word = None
current_count = 0
word = None
dictionary = {}
for line in sys.stdin:
    line = line.strip()
    word, count, date = line.split('\t', 2)
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
        if dictionary[date] is None:
            dictionary[date] = count
        else:
            new_count = int(dictionary[date]) + count
            dictionary[date] = new_count
    else:
        if current_word and current_count>100000:
            print('{:d}\t{:s}'.format(current_count, current_word)),
            for key in dictionary:
                print("{:s}\t{:d}".format(key, dictionary[key]))
        elif current_word:
            print('{:d}\t{:s}'.format(current_count, current_word))
        current_word = word
        current_count = count

if current_word == word:
    print('{:d}\t{:s}'.format(current_count, current_word))
