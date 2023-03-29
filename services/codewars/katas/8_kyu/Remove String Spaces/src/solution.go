package src

func NoSpace(word string) string {
	var resultant_string string
	for _, letter := range word {
		if string(letter) != " " {
			resultant_string += string(letter)
		}
	}

	return resultant_string
}
