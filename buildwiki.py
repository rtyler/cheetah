#!/usr/bin/env python

import sys
import os

def fullpath(folder, file):
	return '%s%s%s' % (folder, os.path.sep, file)

def main():
    print '==> Generating Python files'
    for paths, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.tmpl'):
                os.system('cheetah compile %s' % fullpath(paths, file))
    print '==> Generating HTML files'
    for paths, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.tmpl'):
                os.system('python %(file)s.py > %(file)s.html' % {'file' : fullpath(paths, file[:-5])})
    return 0

if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
