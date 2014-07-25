#!/usr/bin/python
import fileinput
import sys

# states
NORMAL = 0
DQ = 1
SQ = 2
DQ_ESC = 3
SQ_ESC = 4

for line in fileinput.input():
    state = NORMAL
    for char in line:
        sys.stdout.write(char)

        if state==NORMAL:
            if char == '"':
                state = DQ
            elif char == "'":
                state = SQ
            elif char == ";":
                sys.stdout.write("\n")
        elif state==DQ:
            if char == "\\":
                state = DQ_ESC
            elif char == '"':
                state = NORMAL
        elif state==SQ:
            if char == "\\":
                state = SQ_ESC
            elif char == "'":
                state = NORMAL
        elif state==DQ_ESC:
            state = DQ
        elif state==SQ_ESC:
            state = SQ
