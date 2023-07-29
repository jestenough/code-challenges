package src

import (
	"math"
	"strconv"
)

func fillPossibleLastNumbersOfNumbers(numbers *map[int][]int) {
	/*
			map[
				0:[0]
				1:[1]
				2:[6 2 4 8]
				3:[1 3 9 7]
				4:[6 4]
				5:[5]
				6:[6]
				7:[1 7 9 3]
				8:[6 8 4 2]
				9:[1 9]
		]
	*/
	for i := 0; i < 10; i++ {
		var nums []int
		setNums := make(map[int]struct{})
		for j := 4; j <= 10; j++ {
			lastNum := int(math.Pow(float64(i), float64(j))) % 10
			if _, ok := setNums[lastNum]; ok {
				continue
			} else {
				nums = append(nums, lastNum)
			}
			setNums[lastNum] = struct{}{}
		}
		(*numbers)[i] = append((*numbers)[i], nums...)
	}
}

func parseLastTwoDigits(s string) int {
	if len(s) > 1 {
		lastTwoDigits, _ := strconv.Atoi(s[len(s)-2:])
		return lastTwoDigits
	}
	num, _ := strconv.Atoi(s)
	return num
}

func LastDigit(value, pow string) int {

	numbers := map[int][]int{}
	fillPossibleLastNumbersOfNumbers(&numbers)

	intNumber := parseLastTwoDigits(value)
	powNumber := parseLastTwoDigits(pow)
	lastNum := intNumber % 10

	if lastNum == 0 {
		return 0
	}

	valuesLen := len(numbers[lastNum])
	numPos := powNumber % valuesLen

	return numbers[lastNum][numPos]
}
