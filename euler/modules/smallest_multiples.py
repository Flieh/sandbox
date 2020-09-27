"""recursively test if targ is evenly divisible by all values divs and lower"""


def div_all(divs, targ):
    """recursively test if targ is evenly
    divisible by all values divs and lower"""
    if divs == 1:
        return True
    if targ % divs == 0:
        return div_all(divs - 1, targ)
    return False
