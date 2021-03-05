from math import log2


def basic(v):
    return v, v, v


def banded(v):
    r = int(log2(v) * 256) % 256
    g = int(log2(v) * 256) % 256
    b = int(log2(v) * 256) % 256
    return r, g, b
