import dill
import pickle

class Flieh():
    a = 1
    b = '1'
    c = [1,2]
    d = (3,4)
    e = {'one': 'apple', 'two': 'pear'}

class Foobar:
    def __init__(self):
        self.a = 35
        self.b = 'test'
        self.c = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes

def pkl_ex_one():
    flieh_obj = Flieh()
    print(f"property e of flieh_obj:\n{flieh_obj.e}\n")
    flieh_obj_pkl = pickle.dumps(flieh_obj)
    flieh_obj.e = None
    flieh_obj = pickle.loads(flieh_obj_pkl)
    print(f"property e of flieh_obj:\n{flieh_obj.e}\n")
    return 1

def pkl_ex_two():
    square = lambda x : x * x
    return dill.dumps(square)

def pkl_ex_three():
    my_foobar = Foobar()
    my_pkl_str = pickle.dumps(my_foobar)
    my_foobar = pickle.loads(my_pkl_str)
    return my_foobar


def main():
    return pkl_ex_three().c

print(main())
