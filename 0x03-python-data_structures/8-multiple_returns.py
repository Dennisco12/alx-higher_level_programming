#!/usr/bin/python3

def multiple_returns(sentence):
    '''A function that returns a tuple with the length of a string and its first char'''

    if sentence:
        first = sentence[0]
        n = len(sentence)
    else:
        first = None
        n = 0

    return n, first
