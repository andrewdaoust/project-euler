package main

func Problem002(x int) int {
	sum, fib1, fib2 := 2, 1, 2
	for fib2 < x {
		// Get next Fibonacci number
		f := fib1 + fib2

		// Set Fibonacci numbers for next iteration
		fib1 = fib2
		fib2 = f

		if f % 2 == 0 {
			sum += f
		}
	}
	return sum
}
