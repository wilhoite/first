#!/usr/bin/env python
'''
Corrects / enforces curly brace rule.
AUTHOR: Frances Wilhoite frances.wilhoite@bmwna.com
'''
import sys, os

def main():
    filename = raw_input('Enter a file name: ')
    file = open(filename, 'r')

    lines = file.readlines()
    file.close()
    prev_line = lines[0]
    for j in range(0, 2):
        for i in range(1, len(lines)):
            if i < len(lines):
                line = lines[i].split()
                if len(prev_line) == 1 and prev_line[0] == '}' and '{' in line[-1:]:
                    prev_line = ''.join(prev_line) + " ".join([''] + line) + '\r\n'
                    del lines[i]
                    lines[i-1] = prev_line
                    print prev_line
                if len(line) == 1 and line[0] == '{':
                    prev_line = ' '.join(prev_line) + " ".join([''] + line) + '\r\n'
                    del lines[i]
                    lines[i-1] = prev_line
                    print prev_line
                prev_line = line
            else:
                break

    file_rewrite(filename, lines)

def file_rewrite(filename, file_replacement):
    file = open(filename, 'w+')
    for line in file_replacement:
        file.write(line)
    file.close()

if __name__ == '__main__':
    main()
