#!/usr/bin/env python3

import argparse

TMP_FILE = '/tmp/_counter_'

parser = argparse.ArgumentParser(description='Output a new number each time is invoked')
parser.add_argument('-r', '--reset', help='Sets the counter to 0', action='store_true', default=False)
args = parser.parse_args()

current = 0

if not args.reset:
    with open(TMP_FILE, 'r') as f:
        try:
            current = int(f.read())
        except Exception:
            pass
    current += 1
    
with open(TMP_FILE, 'w') as f:
    f.write(str(current))

if not args.reset:
    print(current)
