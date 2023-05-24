package src

func subtractProductAndSum(n int) int {
	sumOfDigits, productOfDigits := 0, 1

	for n > 0 {
		digit := n % 10
		n /= 10

		sumOfDigits += digit
		productOfDigits *= digit
	}

	return productOfDigits - sumOfDigits
}
