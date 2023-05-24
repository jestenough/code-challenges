package src

func interpret(command string) (output string) {
	for i := 0; i < len(command); i++ {
		if command[i] == 'G' {
			output += "G"
		} else if command[i] == '(' && command[i+1] == ')' {
			output += "o"
			i += 1
		} else if command[i] == '(' && command[i+1] == 'a' {
			output += "al"
			i += 3
		}
	}
	return
}
