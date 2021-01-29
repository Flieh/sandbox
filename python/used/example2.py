#!/usr/bin/python

import os

def get_path(filename):
    """return files path or empty string if no path"""
    head, tail = os.path.split(filename)
    breakpoint()
    return head

filename = __file__
print(f'path = {get_path(filename)}')
    
