import numpy as np
import cv2


def im_components(file: str):
    """

    :param file: the path of the image file
    :return: three component of an image
    """
    image = np.array(cv2.imread(file))
    line, column, deep = image.shape
    r = np.array(line, column, deep, dtype=int)
    g = np.array(line, column, deep, dtype=int)
    b = np.array(line, column, deep, dtype=int)
    for i in range(line):
        for j in range(column):
            r[i, j, 0] = image[i, j, 0]
            g[i, j, 1] = image[i, j, 1]
            b[i, j, 2] = image[i, j, 2]
    return r, g, b


def histogram(image: np.array()):
    """
    """
    line, column, deep = image.shape
    ng = np.array(line, column)
    histo = np.array(255)
    for i in range(line):
        for j in range(column):
            ng[i, j] = int((image[i, j, 0] + image[i, j, 1] + image[i, j, 2])/3)
    for k in range(255):
        somme = 0
        for i in range(line):
            for j in range(column):
                if ng[i, j] == k:
                    somme += 1
        histo[k] = somme


def cumulate_histogram(histo: np.array()):
    """
    :param histo: the histogram of an image use to calculate de cumulated histogram
    :return: an array of histogram cumulated
    """
    cumulus = np.array(255)
    cumulus[0] = histo[0]
    for i in range(1, 255):
        cumulus[i] = cumulus[i-1] + histo[i]
    return cumulus


def binary(path: str):
    """

    :param path: The path of the file
    :return: a binary image
    """
    image = np.array(cv2.imread(path, 0))
    line, column = image.shape
    binary = np.array(line, column)
    level = 0
    for i in range(line):
        for j in range(column):
            s = s + image[i, j]
    level = s/(line*column)
    for i in range(line):
        for j in range(column):
            if image[i, j] < level:
                binary[i, j] = 0
            else:
                binary[i, j] = 1
    return binary


def luminosity(image: np.array, value: int):
    """

    :param image: The array of image
    :param value: the luminosity to add
    :return:
    """
    line, column = image.shape
    lumino = np.array(line, column)
    for i in range(line):
        for j in range(column):
            if (image[i, j] + value ) > 255:
                lumino[i, j] = 255
            elif (image[i, j] + b) < 0:
                lumino[i, j] = 0
            else:
                lumino[i, j] = image[i, j] + b
    return lumino


def contrast(image: np.array()):
    """

    :param image:
    :return:
    """
    line, column = image.shape
    min_ = np.min(image)
    max_ = np.max(image)
    contrast = np.array(line, column)
    for i in range(line):
        for j in range(column):
            contrast = 255*(image[i, j] - min_)/(max_ - min_)

    return contrast



