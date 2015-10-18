#!/usr/bin/env python

import socket

def print_remote_machine_info():
    remote_host = "www.python.org"
    try:
        print "IP Address of %s: %s" %(remote_host, socket.gethostbyname(remote_host))
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

if __name__ == "__main__":
    print_remote_machine_info()
