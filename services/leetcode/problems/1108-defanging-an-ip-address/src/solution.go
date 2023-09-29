package src

func defangIPaddr(address string) string {
	output := ""
	for _, v := range address {
		if string(v) == "." {
			output += "[.]"
			continue
		}
		output += string(v)
	}

	return output
}
