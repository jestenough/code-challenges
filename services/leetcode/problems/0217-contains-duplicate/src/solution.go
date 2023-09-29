package src

func ContainsDuplicate(nums []int) bool {
	uniqueNumbers := make(map[int]bool)
	for _, num := range nums {
		if _, ok := uniqueNumbers[num]; ok {
			return true
		} else {
			uniqueNumbers[num] = true
		}
	}

	return false
}
