package src

// https://leetcode.com/problems/valid-anagram/

import (
	"unicode/utf8"
)

func IsAnagram(s string, t string) bool {
	if utf8.RuneCountInString(s) != utf8.RuneCountInString(t) {
		return false
	}

	sLetters := make(map[uint8]int)
	tLetters := make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		if val, ok := sLetters[s[i]]; ok {
			sLetters[s[i]] = val + 1
		} else {
			sLetters[s[i]] = 0
		}

		if val, ok := tLetters[t[i]]; ok {
			tLetters[t[i]] = val + 1
		} else {
			tLetters[t[i]] = 0
		}
	}

	if len(sLetters) != len(tLetters) {
		return false
	}

	for key, sValue := range sLetters {
		if tValue, ok := tLetters[key]; !ok || sValue != tValue {
			return false
		}
	}

	return true
}
