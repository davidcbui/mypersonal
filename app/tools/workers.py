# Mainly for parallel task using multiprocessing
from multiprocessing import Pool


class Workers:
    def __init__(self, count):
        self.count = count

    def sqr(x):
        return x ** 2

    def doWork(count):
        p = Pool(self.count)
        p.map(sqr(9))
