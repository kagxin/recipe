package main

import (
	"fmt"
)

func main() {
	var myArray [10]int = [10]int{1, 2, 34, 5, 6, 7, 7}
	var mySlice []int = myArray[:5]
	mySlice2 := make([]int, 4, 5)

	fmt.Println("asdf")
	for i := 0; i < len(mySlice); i++ {
		fmt.Println(mySlice[i])
	}
	for _, v := range mySlice {
		fmt.Println(v)
	}
	mySlice2 = append(mySlice2, 123, 2, 3)
	mySlice2 = append(mySlice2, mySlice...)
	fmt.Println(len(mySlice2), cap(mySlice2))
	fmt.Println(mySlice2)
}
