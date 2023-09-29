package src

func getConcatenation(nums []int) []int {
	length := len(nums)
	output := make([]int, length*2)

	for i, v := range nums {
		output[i] = v
		output[i+length] = v
	}

	return output
}
