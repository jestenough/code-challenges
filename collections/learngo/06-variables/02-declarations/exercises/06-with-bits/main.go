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
// EXERCISE: Declare with bits
//
//  1. Declare a few variables using the following types
//    int
//    int8
//    int16
//    int32
//    int64
//    float32
//    float64
//    complex64
//    complex128
//    bool
//    string
//    rune
//    byte
//
// 2. Observe their output
//
// 3. After you've done, check out the solution
//    and read the comments there
//
// EXPECTED OUTPUT
//  0 0 0 0 0 0 0 (0+0i) (0+0i) false 0 0
//  ""
// ---------------------------------------------------------

func main() {
	// integers
	var i int
	var i8 int8
	var i16 int16
	var i32 int32
	var i64 int64

	// floa
	var f32 float32
	var f64 float64

	// complex
	var com64 complex64
	var com128 complex128

	// boolean
	var bl bool

	// string types
	var s string
	var r rune
	var b byte

	fmt.Println(
		i,
		i8,
		i16,
		i32,
		i64,
		f32,
		f64,
		com64,
		com128,
		bl,
		s,
		r,
		b,
	)
}
