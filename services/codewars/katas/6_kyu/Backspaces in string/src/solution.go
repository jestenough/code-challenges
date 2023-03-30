package src

func CleanString(s string) string {
	output := ""
	for _, v := range s {
		if v == '#' {
			if len(output) == 0 {
				continue
			}
			output = output[:len(output)-1]
		} else {
			output += string(v)
		}
	}

	return output
}
