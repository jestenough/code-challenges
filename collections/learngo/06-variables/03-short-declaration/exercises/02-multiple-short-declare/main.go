// Copyright © 2018 Inanc Gumus
// Learn Go Programming Course
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//
// For more tutorials  : https://learngoprogramming.com
// In-person training  : https://www.linkedin.com/in/inancgumus/
// Follow me on twitter: https://twitter.com/inancgumus

package main

import "fmt"

// ---------------------------------------------------------
// EXERCISE: Multiple Short Declare
//
//  Declare two variables using multiple short declaration
//
// EXPECTED OUTPUT
//  14 true
// ---------------------------------------------------------

func main() {
	ifMyGfAgeIs, willTheyPutMeInJall := 14, true
	fmt.Println(ifMyGfAgeIs, willTheyPutMeInJall)

}
