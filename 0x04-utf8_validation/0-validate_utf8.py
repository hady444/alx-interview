#!/usr/bin/python3
"""Solving Validate UTF-8 Problem Module"""


def validUTF8(data):
    bytes = 0
    for num in data:
        byte = num & 0xFF
        if bytes == 0:
            if byte & 0b10000000 == 0b00000000:
                continue
            elif byte & 0b11100000 == 0b11000000:
                bytes = 2
            elif byte & 0b11110000 == 0b11100000:
                bytes = 3
            elif byte & 0b11111000 == 0b11110000:
                bytes = 4
            else:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            bytes -= 1
    return bytes == 0
