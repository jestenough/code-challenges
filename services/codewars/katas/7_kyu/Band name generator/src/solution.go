package src

import "strings"

func bandNameGenerator(word string) string {

	if word[0] != word[len(word)-1] {
		return "The " + strings.Title(word)
	}

	return strings.Title(word + word[1:])
}
