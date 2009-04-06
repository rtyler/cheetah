#!/usr/bin/env python

import sys
import os

def main():
    print '==> Generating Python files'
    files = os.listdir('.')
    for file in files:
        if file.endswith('.tmpl'):
            os.system('cheetah compile %s' % file)
    print '==> Generating HTML files'
    for file in files:
        if file.endswith('.tmpl'):
            os.system('python %(file)s.py > %(file)s.html' % {'file' : file[:-5]})
    return 0

if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
