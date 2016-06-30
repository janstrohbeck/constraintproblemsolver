def flatten(nested):
    if type(nested) == list or type(nested) == tuple:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    else:
        yield nested
