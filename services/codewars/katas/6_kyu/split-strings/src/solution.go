package src

func Solution(str string) []string {

	length := len(str)
	if length%2 != 0 {
		length++
	}

	runes := []rune(str)
	pairs := make([]string, 0, length/2)

	for i := 0; i < len(runes); i += 2 {
		if i+1 < len(runes) {
			pairs = append(pairs, string(runes[i])+string(runes[i+1]))
		} else {
			pairs = append(pairs, string(runes[i])+"_")
		}
	}

	return pairs
}
