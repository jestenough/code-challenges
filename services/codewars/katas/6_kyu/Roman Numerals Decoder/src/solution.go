package src

var romanNumbers = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func Decode(roman string) (res int) {
	prevValue := 0

	for _, romanNumber := range roman {
		currentValue := romanNumbers[romanNumber]
		if prevValue < currentValue {
			res += currentValue - prevValue*2
		} else {
			res += currentValue
		}

		prevValue = currentValue
	}

	return
}
