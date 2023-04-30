"""peak module
Technical interview Preparation
"""


def find_peak(list_of_integers):
    """find_peak function
    Args:
        - list_of_integers: contains list of integers
    """
    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
