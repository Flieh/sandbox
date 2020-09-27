'''remarks'''
def gen_one(limit):
    '''first get example'''
    for i in range(limit):
        yield i ** i
