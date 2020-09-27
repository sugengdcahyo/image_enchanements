from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Histogram:
    def __init__(self, *args, **kwargs):
        pass

    def count_elements(self, seq, *args, **kwargs) -> dict:
        hist={}
        for x in range(seq.shape[0]):
            for i in seq[x]:
                hist[i] = hist.get(i, 0) + 1
        return hist

    def sorted_by_keys(self, seq={}, *args, **kwargs) -> dict:
        dict_items = seq.items()
        sorted_items = sorted(dict_items)
        return sorted_items

class Plot(Histogram):
    def __init__(self, seq={}):
        self.seq = seq

    def plot_hist(self):
        seq = self.seq
        plt.plot(data=seq)
        plt.show()

    def plot_images(self, rgb):
        img = plt.imshow(rgb)
        # plt.rcParams['figure.dpi'] = 100
        return img 
    
        
