#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        return_tuple = (len(sentence), sentence[0])
        return return_tuple

    return (0, None)
