package src

import "fmt"

const secondsPerHour = 3600
const secondsPerMinute = 60

func HumanReadableTime(seconds int) string {
	hours, minuteRemainder := seconds/secondsPerHour, seconds%secondsPerHour
	minutes, secondsRemainder := minuteRemainder/secondsPerMinute, minuteRemainder%secondsPerMinute
	humanReadableOutput := fmt.Sprintf("%02d:%02d:%02d", hours, minutes, secondsRemainder)
	return humanReadableOutput
}
