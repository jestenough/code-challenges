package src

func finalValueAfterOperations(operations []string) int {
	var x int = 0

	for _, v := range operations {
		operator := string(v[1])
		if operator == "-" {
			x--
		} else if operator == "+" {
			x++
		}
	}

	return x

}
