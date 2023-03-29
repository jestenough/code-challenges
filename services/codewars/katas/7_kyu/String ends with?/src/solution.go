package src

func solution(str, ending string) bool {

	flag := true
	if len(str) == 0 {
		return str == ending
	}

	for st, en := len(str), len(ending); en > 0; st, en = st-1, en-1 {
		if st-1 < 0 || en-1 < 0 || str[st-1] != ending[en-1] {
			flag = false
			break
		}
	}

	return flag

	// BEST SOLUTION
	// return len(str) >= len(ending) && str[len(str) - len(ending):] == ending

}
