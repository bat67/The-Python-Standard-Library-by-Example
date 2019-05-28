#!/usr/bin/env python3
"""Create test data for the glob examples.
"""
#end_pymotw_header
import os


def mkfile(filename):
    print(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n')


print('dir')
os.mkdir('dir')

mkfile('dir/file.txt')
mkfile('dir/file1.txt')
mkfile('dir/file2.txt')
mkfile('dir/filea.txt')
mkfile('dir/fileb.txt')
mkfile('dir/file?.txt')
mkfile('dir/file*.txt')
mkfile('dir/file[.txt')

print('dir/subdir')
os.mkdir('dir/subdir')

mkfile('dir/subdir/subfile.txt')
