import os import lisdir
import os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Histogram:
    def __init__(self, *args, **kwargs):
        pass

    def count_elements(self, seq, *args, **kwargs):
        hist={}
        for x in range(seq.shape[0]):
            for i in seq[x]:
                hist[i] = hist.get(i, 0) + 1
        return hist

    def sorted_by_keys(self, seq={}, *args, **kwargs):
        dict_items = seq.items()
        sorted_items = sorted(dict_items)
        return dict(sorted_items)

    def plot_hist(self, ):
        
