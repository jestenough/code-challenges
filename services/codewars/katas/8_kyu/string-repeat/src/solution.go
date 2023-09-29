package src

func RepeatStr(repetitions int, value string) string {

	output_string := value
	for i := 1; i < repetitions; i += 1 {
		output_string += value
	}

	return output_string
}
