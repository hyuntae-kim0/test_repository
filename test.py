#함수 사용
#코드 사용
import timeit


class test:
    def __init__(self):
        self.test = 1

    def double(self):
        self.test *= 2
        print(self.test)


setup = '''from __main__ import test'''
test = test()
t = timeit.timeit(stmt='test.double()', setup=setup, number=1)
print(t)
test.double()
