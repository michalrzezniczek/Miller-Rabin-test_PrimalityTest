__author__ = 'Michal Rzezniczek'


def to_bin(dec_exponent):
    bin_exponent = []
    while dec_exponent > 0:
        bin_exponent.insert(0, dec_exponent % 2)
        dec_exponent /= 2
    if len(bin_exponent) == 0:
        return [0]
    return bin_exponent

