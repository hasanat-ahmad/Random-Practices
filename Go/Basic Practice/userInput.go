package main

import (
	"fmt"
	"bufio"
	"os"
)

func takingInput() {
	fmt.Print("Enter your name: ")
	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	fmt.Println("Hello, " + name)


}
