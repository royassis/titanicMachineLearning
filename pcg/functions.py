from os import walk
import re
import datetime
import numpy as np

#Define an iterative file name for scv files created
def savetofile(dframe, score_dict, dir):

    #Get a
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        f.extend(filenames)
        break

    for filename in f:
        number = 0
        match = re.match("predictions_(\d+).*", filename)
        if match == None:
            continue
        if int(match.group(1)) > number:
            number = match.group(1)
    number = int(number) + 1

    filename = "predictions"
    number = number.__str__()
    date = datetime.date.today().strftime("%d-%m-%y")
    score = np.round(score_dict["NN"],2).__str__()
    suffix = "csv"

    str = '__'.join([filename, number, date, score])
    path = '/'.join([dir, str])
    path = '.'.join([path, suffix])

    dframe.to_csv(path, index=False)

