from os import listdir
from os.path import isfile, isdir, join

class DataManager:
    def __init__(self, datapath = '../../datasets/samples/', *args, **kwargs):
        try:
            self.datapath = datapath
        except:
            return "Path isn't callable!"

    def dataset(self)->list:
        return listdir(self.datapath)
        