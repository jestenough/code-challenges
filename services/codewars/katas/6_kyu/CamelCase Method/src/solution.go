package src

import "strings"

func CamelCase(s string) string {
	output := ""
	word := ""
	for i := 0; i < len(s); i++ {
		if string(s[i]) == " " {
			if len(word) > 1 {
				output += strings.ToTitle(string(word[0])) + word[1:]
			}
			word = ""
		} else {
			word += string(s[i])
		}
	}

	if word != "" {
		output += strings.ToTitle(string(word[0])) + word[1:]
	}

	return output
}
