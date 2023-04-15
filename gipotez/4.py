import ctypes

test = ctypes.CDLL('./calculate_primes.so')

n = int(input("Введи число n: "))

m = int(input("Введи число m: "))

arr = (ctypes.c_int * m)()

for i in range(len(arr)):
	arr[i] = i

test.calculate_primes(arr,m)

numbers = []

for i in range(len(arr)):
	if (arr[i] != 1) and (arr[i] != 0):
		numbers.append(arr[i])

s = 0

buffer = 0

maxx = 1000000

for i in range(n, m+1):
	if i % 2 == 0:
		print (i, end = ' ')
		for x in range(len(numbers)):
			for y in range(len(numbers)):
				if ((numbers[x] != 1) and (numbers[y] !=1) and (numbers[x] + numbers[y] == i)):
					s += 1
					if ((numbers[x] != numbers[y]) and ((numbers[x]+numbers[y]) == (numbers[y]+numbers[x]))):
						buffer +=1
					if (numbers[x] <= maxx):
						num1 = numbers[x]
						num2 = numbers[y]
						maxx = numbers[x]
		s = s - buffer // 2

		print(s,num1,num2)

		s = 0 

		buffer = 0

		maxx = 1000000