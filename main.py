class GeneratorIterator:
    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(16):
            yield i

my_iterable = GeneratorIterator()

for value in my_iterable:
    print(value)