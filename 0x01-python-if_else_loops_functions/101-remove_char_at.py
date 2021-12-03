#!/usr/bin/python3
def remove_char_at(str, n):
    aux = ""
    i = 0
    while i < len(str):
        if i == n:
            i += 1
        aux += str[i]
        i += 1
    return aux
