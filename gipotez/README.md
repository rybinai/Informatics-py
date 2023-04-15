Гипотеза Гольдбаха.

В программе реализована проверка гипотезы Гольдобаха на языке Python, но реализация функции calculate_primes сделана на языке C. 

Чтобы запустить файл, соберите библиотеку.

gcc -fPIC -shared -o calculate_primes.so calculate_primes.c

 Для входных данных:

	4 10

должно быть выведно:

	4 1 2 2
	6 1 3 3
	8 1 3 5
	10 2 3 7
	
///

Goldbach's hypothesis.

The program implements the Goldobach hypothesis test in Python, but the implementation of the calculate_primes function is done in C.

To run the file, build the library.

gcc -fPIC -shared -o calculate_primes.so calculate_primes.c

  For input data:

4 10

should output:

4 1 2 2
6 1 3 3
8 1 3 5
10 2 3 7

