// Copyright © 2018 Inanc Gumus
// Learn Go Programming Course
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//
// For more tutorials  : https://learngoprogramming.com
// In-person training  : https://www.linkedin.com/in/inancgumus/
// Follow me on twitter: https://twitter.com/inancgumus

package main

import (
	"fmt"
	"os"
	"strconv"
)

// ---------------------------------------------------------
// STORY
//  You're curious about the richter scales. When reporters
//  say: "There's been a 5.5 magnitude earthquake",
//
//  You want to know what that means.
//
//  So, you've decided to write a program to do that for you.
//
// EXERCISE: Richter Scale
//
//  1. Get the earthquake magnitude from the command-line.
//  2. Display its corresponding description.
//
// ---------------------------------------------------------
// MAGNITUDE                    DESCRIPTION
// ---------------------------------------------------------
// Less than 2.0                micro
// 2.0 and less than 3.0        very minor
// 3.0 and less than 4.0        minor
// 4.0 and less than 5.0        light
// 5.0 and less than 6.0        moderate
// 6.0 and less than 7.0        strong
// 7.0 and less than 8.0        major
// 8.0 and less than 10.0       great
// 10.0 or more                 massive
//
// EXPECTED OUTPUT
//  go run main.go
//    Give me the magnitude of the earthquake.
//
//  go run main.go ABC
//    I couldn't get that, sorry.
//
//  go run main.go 0.5
//    0.50 is micro
//
//  go run main.go 2.5
//    2.50 is very minor
//
//  go run main.go 3
//    3.00 is minor
//
//  go run main.go 4.5
//    4.50 is light
//
//  go run main.go 5
//    5.00 is moderate
//
//  go run main.go 6
//    6.00 is strong
//
//  go run main.go 7
//    7.00 is major
//
//  go run main.go 8
//    8.00 is great
//
//  go run main.go 11
//    11.00 is massive
// ---------------------------------------------------------

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Give me the magnitude of the earthquake.")
		return
	}

	var (
		value float64
		err   error
	)

	if value, err = strconv.ParseFloat(os.Args[1], 8); err != nil {
		fmt.Println("I couldn't get that, sorry.")
		return
	}

	var valueForMessage string
	switch r := value; {
	case r < 2:
		valueForMessage = "micro"
	case r >= 2 && r < 3:
		valueForMessage = "very minor"
	case r >= 3 && r < 4:
		valueForMessage = "minor"
	case r >= 4 && r < 5:
		valueForMessage = "light"
	case r >= 5 && r < 6:
		valueForMessage = "moderate"
	case r >= 6 && r < 7:
		valueForMessage = "strong"
	case r >= 7 && r < 8:
		valueForMessage = "major"
	case r >= 8 && r < 10:
		valueForMessage = "great"
	default:
		valueForMessage = "massive"
	}

	fmt.Printf("%.2f is %s\n", value, valueForMessage)
}
