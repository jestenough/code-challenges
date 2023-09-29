package main

import (
	"fmt"
	"strings"
)

type timeComponent struct {
	value        int64
	verboseName  string
	pluralSuffix string
}

func FormatDuration(seconds int64) string {
	if seconds < 0 {
		return "now"
	}

	const (
		secondsPerYear   = 31536000
		secondsPerDay    = 86400
		secondsPerHour   = 3600
		secondsPerMinute = 60
	)
	years, yearsRemainder := seconds/secondsPerYear, seconds%secondsPerYear
	days, hoursRemainder := yearsRemainder/secondsPerDay, yearsRemainder%secondsPerDay
	hours, minuteRemainder := hoursRemainder/secondsPerHour, hoursRemainder%secondsPerHour
	minutes, secondsRemainder := minuteRemainder/secondsPerMinute, minuteRemainder%secondsPerMinute

	timeComponents := []timeComponent{
		{years, "year", "s"},
		{days, "day", "s"},
		{hours, "hour", "s"},
		{minutes, "minute", "s"},
		{secondsRemainder, "second", "s"},
	}

	var formattedComponents []string
	for _, component := range timeComponents {
		if formattedValue := formatTimeComponent(component); formattedValue != "" {
			formattedComponents = append(formattedComponents, formattedValue)
		}
	}

	separatedByCommaValues := strings.Join(formattedComponents, ", ")
	if lastCommaIndex := strings.LastIndex(separatedByCommaValues, ", "); lastCommaIndex != -1 {
		separatedByCommaValues = separatedByCommaValues[:lastCommaIndex] + " and" + separatedByCommaValues[lastCommaIndex+1:]
	}

	return separatedByCommaValues
}

func formatTimeComponent(component timeComponent) string {
	if component.value == 0 {
		return ""
	} else if component.value > 1 {
		return fmt.Sprintf("%d %s%s", component.value, component.verboseName, component.pluralSuffix)
	}

	return fmt.Sprintf("%d %s", component.value, component.verboseName)
}
