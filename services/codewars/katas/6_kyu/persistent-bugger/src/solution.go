package src

func Persistence(n int) int {
	count := 0

	for n >= 10 {
		multiply := 1
		for n != 0 {
			multiply *= n % 10
			n /= 10
		}
		n = multiply
		count++
	}

	return count
}
