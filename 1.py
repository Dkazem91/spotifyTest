#!/usr/bin/python3
"""Sort the letters in the string s by the order they occur in the string t."""


def sortByStrings(s, t):
    if type(s) is str and type(t) is str:
        return ("").join(ltr * s.count(ltr) for ltr in t if ltr in s)
