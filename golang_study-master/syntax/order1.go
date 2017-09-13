package main

import (
	"fmt"
)

func example(x int) int {
	if x == 0 {
		return 5
	} else {
		return x
	}
}

func main() {
	a := 1
	b := 2
	if a > b {
		fmt.Println("a>b.")
	} else {
		fmt.Println("b>a.")
	}

	fmt.Println(example(0))

}
