package src

func DigitalRoot(n int) int {

	if n < 10 {
		return n
	}

	for n >= 10 {
		sum := 0
		for n > 0 {
			digit := n % 10
			sum += digit
			n /= 10
		}
		n = sum
	}

	return n

}
