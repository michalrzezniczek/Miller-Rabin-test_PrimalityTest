#!/usr/bin/env python
import random


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


def miller_rabin_test(testing_number):
	if testing_number % 2 == 0:
		return 0 #is not a prime number
	else if testing_number < 2:
		return -1 #wrong input
    q = testing_number - 1
    d = 0
    ##testing_number = 2^{d}*q
    while (q % 2) == 0:
        d += 1
        q /= 2
    #print "%d - 1 = 2^{%d} * %d \t\t d = %d\tq = %d" % (testing_number, d, q, d, q)
    a = random.randint(2, testing_number - 1)
    sequence_element = modularPower(a, q, testing_number)
    #print "%d^{%d} mod(%d) = %d" % (a, q, testing_number, sequence_element)
    if (sequence_element == 1) or (sequence_element == (testing_number - 1)):
        return 1 #is prime number
    j = 2
    while (j <= d) and (sequence_element != (testing_number - 1)):
        sequence_element = modularPower(sequence_element, 2, testing_number)
        print "%d^{%d} mod(%d) = %d" % (a, q*j, testing_number, sequence_element)
        if sequence_element == (-1 % testing_number):
            return 1 #is prime number
        j += 1
    return 0 #is not prime number