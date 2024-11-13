package main

func Problem001(x int) int {
	sum := 0
	for i := range x {
		if i % 3 == 0 || i % 5 == 0 {
			sum += i
		}
	}
	return sum
}