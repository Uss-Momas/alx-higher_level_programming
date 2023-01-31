#!/usr/bin/python3
""" Module Name: 5-text_indentation

Contains functions to manage a text acording to a situation given

Functions:
    text_indentation: indent a text acording to a especific char
"""


def text_indentation(text):
    """Function text_indentation
    Prints a text with 2 new line after these chars: '.' , '?' and ':'

    Args:
        text: the text to be indented

    Returns:
        Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    lines = []
    line = ""
    for char in text:
        if char in ['.', '?', ':']:
            line += char
            lines.append(line)
            line = ""
            continue
        line += char
    lines.append(line)

    last_line_idx = len(lines) - 1
    for i in range(len(lines)):
        if i != last_line_idx:
            print(lines[i].strip())
            print()
            continue
        print(lines[i].strip(), end="")
