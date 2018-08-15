# trying master generator concept
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i

        else:
            raise StopIteration()

    @staticmethod
    def xrange(n):
        i = 0

        while i < n:
            yield i
        i += 1

    @staticmethod
    def gen_num(total_no):
        n = 0
        while n < total_no:
            yield n
            n += 1

    @staticmethod
    def repeat(count, name):
        for i in range(count):
            print(name)

