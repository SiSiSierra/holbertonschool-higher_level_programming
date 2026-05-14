#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        fchar = 0
    else:
        fchar = sentence[0]
    return (len(sentence), fchar)
