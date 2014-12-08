Primality Test
===============
University task.

Implemented (in Python) Miller-Rabin test and fast modular exponentiation.

1. Usage:
	You have to call function miller_rabin_test(testing_number) with the paramter equal to the number which you want to test

	n = input("n = ")
	output = miller_rabbin_test(n)
    if output == 1:
        print "%d probably is a prime number" % n
    else if output == 0:
        print "%d is not a prime number" % n
    else:
    	print "%d is wrong number"

2. Output:
   -1 	<=> wrong testing_number. E.g. testing_number less than 2
	0 	<=> testing_number is not a prime number
	1 	<=> testing_number probably is a prime number