#!/usr/bin/env python

import sys
import os
import SimpleHTTPServer

def main():
    print '==> Starting wiki server on port 8000'
    try:
        SimpleHTTPServer.test()
    except KeyboardInterrupt:
        print '===> Exiting..'
    return 0

if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
