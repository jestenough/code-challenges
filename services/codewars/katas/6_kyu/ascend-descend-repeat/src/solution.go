package src

import (
	"strconv"
)

func AscendDescend(length, minimum, maximum int) (output string) {
	if length == 0 || maximum < minimum {
		return
	}

	for curNum, step := minimum, 1; len(output) < length; curNum += step {
		output += strconv.Itoa(curNum)

		if maximum == minimum {
			step = 0
		} else if curNum == maximum {
			step = -1
		} else if curNum == minimum {
			step = 1
		}
	}

	return output[:length]
}
