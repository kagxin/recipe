package main

import (
	"fmt"
)

func usage() {
	return
}

func main() {
	var v1 int32 = 10
	var v2 = 10
	v3 := 10
	v4 := 9.9
	const (
		a int = 1 << iota
		b int = 1 << iota
		c int = 1 << iota
	)

	fmt.Println("hello word!")

	fmt.Println(a, b, c)
	fmt.Println(1 << 0)
	if int(v4) > v2 {
		fmt.Println(int(v1) + v2 + v3)
	}
	fmt.Println(int(v4))
	usage()

	var str string = "hello world!"
	fmt.Println(str)
	for i := 0; i < len(str); i++ {
		if str[i] == 'h' {
			fmt.Printf("%c.", str[i])
			fmt.Printf("equel.")
		}
	}
	if 104 == 'h' {
		fmt.Println("104==h")
	}

	for i, ch := range str {
		fmt.Println(i, ch)
	}

}
