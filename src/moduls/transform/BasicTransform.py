from histogram.Histogram import Histogram
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

class BasicTransform(Histogram):
    def __init__(self, *args, **kwargs):
        pass

    def Brightness(self, data, threshold, *args, **kwargs):
        # code brightness manipulations
        pass

    def Contrasts(self, *args, **kwargs):
        # code of contrasts manipulations
        pass

    def rgb2gray(self, img, *args, **kwargs):
        pass
