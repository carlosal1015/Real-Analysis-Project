#!/usr/bin/python
# -*- coding: utf8 -*-

def add1(x):
    return x + 1

if __name__ == "__main__":
    print("Run as program.")
    import sys
    print(add1(float(sys.argv[1])))
