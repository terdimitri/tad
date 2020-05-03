#!/usr/bin/env python
"""An application for storing and managing tasks in a hierarchal manner."""
import argparse
import json




def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['add', 'remove'])

    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
