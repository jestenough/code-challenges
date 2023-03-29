package src

func Grow(arr []int) int {
	var multiply int = 1
	for _, value := range arr {
		multiply *= value
	}
	return multiply
}
