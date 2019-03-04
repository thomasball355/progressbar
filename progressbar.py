# Simple progress bar 20/02/19

import os

def bar(perc, **kwargs):

    """# Default length is 100, no label by default
    # kwargs
            # label;    label for the bar
            # length;   integer as long as you want the bar to be
            # fit;      fits to the width of the terminal

    # usage
            # import progressbar as pb
            #
            # pb.bar(percentage(int from 0 to 100), length = length(int),
            # fit = True/False, label = "label")"""

    tot_len = 100
    label = ""
    char = "="

    try:
        cols, rows = os.get_terminal_size(0)
    except OSError:
        cols, rows = os.get_terminal_size(1)

    print(" ", end = "\r")

    for key, value in kwargs.items():
        if key == "label":
            label = value
        if key == "length":
            tot_len = value
        if key == "fit":
            if value == True:
                tot_len = cols - 9 - len(label)
        if key == "char":
            char = value

    if cols < tot_len + 9 + len(label):
        tot_len = cols - 9 - len(label)

    progress = int(perc * (tot_len/100.0))

    bar = char * progress
    blank = " " * (tot_len - progress)

    outp = "[{}] {}% {}".format(bar+blank, perc, label)
    if perc < 100:
        print(outp, end = "\r")
    else:
        print(outp)
