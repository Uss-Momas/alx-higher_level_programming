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

    new_text = ""
    lines = []
    for char in text:
        if char in ['.', '?', ':']:
            new_text += "?"
        else:
            new_text += char
    new_text += "?"
    line = ""
    i = 0
    for char in new_text:
        if char != '?':
            line += char
        else:
            if i != len(new_text) - 1:
                line += "\n\n"
            lines.append(line)
            line = ""
        i += 1

    for line in lines:
        for i in range(len(line)):
            if i == 0 and line[i] == " ":
                continue
            print(line[i], end="")
