#!/usr/bin/python3
"""Given an encoded string, return its corresponding decoded string"""


def isNumber(x):
    try:
        return int(x)
    except ValueError:
        pass


def decodeString(s):
    letters = list(s.replace("[", "*(").replace("]", ")"))
    for idx, val in enumerate(letters):
        if isNumber(val):
            letters[idx] = "+" + val
        elif val not in "*()":
            letters[idx] = '"{}"'.format(val)
    try:
        return eval(('').join(letters))
    except:
        pass
