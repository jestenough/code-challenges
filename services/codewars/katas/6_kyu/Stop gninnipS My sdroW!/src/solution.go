package src

func MutateString(word string) string {
	output := ""

	if len(word) >= 5 {
		for i := len(word) - 1; i >= 0; i-- {
			output += string(word[i])
		}
	} else {
		output += word
	}

	return output
}

func SpinWords(str string) string {

	word := ""
	output := ""
	for _, letter := range str {

		if letter == ' ' {
			output += MutateString(word) + " "
			word = ""
		} else {
			word += string(letter)
		}
	}

	if len(word) >= 1 {
		output += MutateString(word)
	}

	return output

}
