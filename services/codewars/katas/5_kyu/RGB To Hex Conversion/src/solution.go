package src

import "fmt"

func RGB(r, g, b int) string {
	rgbValidValue := func(val int) int {
		if val < 0 {
			return 0
		}
		if val > 255 {
			return 255
		}
		return val
	}

	return fmt.Sprintf("%02X%02X%02X", rgbValidValue(r), rgbValidValue(g), rgbValidValue(b))
}
