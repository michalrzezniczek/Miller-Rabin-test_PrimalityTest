__author__ = 'Michal Rzezniczek'


def to_bin(dec_exponent):
    bin_exponent = []
    while dec_exponent > 0:
        bin_exponent.insert(0, dec_exponent % 2)
        dec_exponent /= 2
    if len(bin_exponent) == 0:
        return [0]
    return bin_exponent


def modularPower(dec_base, dec_exponent, modulo):
    bin_exponent_reversed = to_bin(dec_exponent)
    bin_exponent_reversed.reverse()
    result = 1
    dec_base %= modulo
    tmp = dec_base
    for bit in bin_exponent_reversed:
        if bit != 0:
            result *= tmp
            result %= modulo
        tmp *= tmp
        tmp %= modulo
    return result