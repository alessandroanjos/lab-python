
class Sequencial():
    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <=6 :
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration


