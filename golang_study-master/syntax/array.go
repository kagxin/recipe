package main

import "fmt"

func modify(array [6]int) {
	array[0] = 10
	fmt.Println(array)
}

func main() {
	array := [6]int{1, 2, 3, 4, 5}
	modify(array)
	fmt.Println(array)
}
