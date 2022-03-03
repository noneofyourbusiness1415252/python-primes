from timeit import timeit

print(
	"Time taken:",
	timeit(
		f"print(primesupto({input('Enter a number to find the primes up to it: ')}))",
		setup="from primes import primesupto",
		number=1,
	),
)
